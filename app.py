import os
import csv
import tempfile
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.units import inch
from PIL import Image as PILImage, ImageDraw, ImageFont
import configparser

temp_file_paths = []
custom_page_width = 255.0
custom_page_height = 165.0
custom_page_size = landscape((custom_page_width, custom_page_height))

config = configparser.ConfigParser()
config.read('config.properties')

id_template_path = config['Properties']['id_template']
csv_file_path = config['Properties']['csv_file']
output_filename = config['Properties']['output_filename']+".pdf"
images_directory = config['Properties']['images_directory']

def create_temporary_image(pil_image):
    """
    Create a temporary file from a PIL Image object and return its path.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        pil_image.save(temp_file.name)
        temp_file_path = temp_file.name
        temp_file_paths.append(temp_file_path)
    return temp_file_path

def truncate_name(name, max_length):
    """
    Truncate the name if it exceeds the maximum length.
    """
    if len(name) > max_length:
        return name[:max_length]
    else:
        return name

doc = SimpleDocTemplate(output_filename, pagesize=custom_page_size, leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)
elements = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        template_image = PILImage.open(id_template_path)
        name_font = ImageFont.truetype("Roboto-Bold.ttf", size=20)
        title_font = ImageFont.truetype("Roboto-Bold.ttf", size=10)
        name = truncate_name(row["Name"], 29)
        title = row["Title"]
        draw = ImageDraw.Draw(template_image)
        draw.text((8, 170), name, font=name_font, fill=(0, 0, 0))
        draw.text((175, 143), title, font=title_font, fill=(0, 0, 0))
        photo_path = row["Location"]
        photo_image = PILImage.open(os.path.join(images_directory, photo_path))
        photo_image = photo_image.resize((100, 120))
        template_image.paste(photo_image, (187, 20))
        temp_file_path = create_temporary_image(template_image)
        elements.append(Image(temp_file_path, 3.375 * inch, 2.125 * inch))
        elements.append(PageBreak())

doc.build(elements)

for temp_file in temp_file_paths:
    print("temp_file", temp_file)
    os.remove(temp_file)

print(f"ID cards have been generated in {output_filename}")
