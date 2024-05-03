import os
import csv
import tempfile
from reportlab.lib.pagesizes import landscape,portrait,letter
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.units import inch
from PIL import Image as PILImage, ImageDraw, ImageFont



temp_file_paths=[]
custom_page_width = 255.0
custom_page_height = 165.0
custom_page_size = landscape((custom_page_width, custom_page_height))

def create_temporary_image(pil_image):
    """
    Create a temporary file from a PIL Image object and return its path.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        pil_image.save(temp_file.name)
        temp_file_path = temp_file.name
        temp_file_paths.append(temp_file_path)
    return temp_file_path

# Set up the PDF document
output_filename = "id_cards.pdf"
doc = SimpleDocTemplate(output_filename, pagesize=custom_page_size, leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)
elements = []

# Open the CSV file and read the data
with open("id_data.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Load the ID template image
        template_image = PILImage.open("id_template.png")
        name_font = ImageFont.truetype("Roboto-Bold.ttf", size=30)
        title_font = ImageFont.truetype("Roboto-Bold.ttf", size=10)
        # Add the name and title to the template image
        name = row["Name"]
        title = row["Title"]
        draw = ImageDraw.Draw(template_image)
        draw.text((8, 170), name, font=name_font, fill=(0, 0, 0))  # Adjust coordinates as needed
        draw.text((175, 143), title, font=title_font, fill=(0, 0, 0))  # Adjust coordinates as needed

        # Add the ID photo to the template image
        photo_path = row["Location"]
        photo_image = PILImage.open(os.path.join("images", photo_path))
        print(os.path.join("images", photo_path))
        photo_image = photo_image.resize((100, 120))  # Adjust size as needed
        template_image.paste(photo_image, (187, 20))  # Adjust coordinates as needed

        # Save the template image to a temporary file
        temp_file_path = create_temporary_image(template_image)

        # Add the image to the PDF elements list
        elements.append(Image(temp_file_path, 3.375 *inch, 2.125 *inch))  # Adjust size as needed

        elements.append(PageBreak())

# Build the PDF document
doc.build(elements)

for temp_file in temp_file_paths:
    print("temp_file", temp_file)
    os.remove(temp_file)

print(f"ID cards have been generated in {output_filename}")