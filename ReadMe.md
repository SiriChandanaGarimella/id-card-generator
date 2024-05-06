**ID CARD GENERATOR**

This code base is to generate the id cards based on the given id template.

All the properties should be given in config.properties file

**config.properties file update**
- **id_template** = Your id template location (Example: /Users/sirichandanagarimella/Documents/id_template.png)
- **csv_file** = The csv file containing the details of name, title(position) and location of images (Example: /Users/sirichandanagarimella/Documents/id_data.csv)
- **output_filename** = The name of the output file that you want it to be generated. Example (id_cards). The file will get generated in the id-card-generator folder.
- **images_directory** = The directory containing the images (Example: /Users/sirichandanagarimella/Documents/images)

**Commands to activate the venv:**

In macOS:
- Setup the venv environment: <code>python3 -m venv venv</code>
- Activate the venv environment: <code>source venv/bin/activate</code>
- Install the requirements: <code>pip install -r requirements.txt</code>

In windows:
- Setup the venv environment: <code>py -m venv venv</code>
- Activate the venv environment: <code>.\venv\Scripts\activate</code>
- Install the requirements: <code>pip install -r requirements.txt</code>

**Command to run the script:**
- In macOS: <code>python3 app.py</code>
- In windows: <code>py app.py</code>

**Sample Output**

<img width="1469" alt="image" src="https://github.com/SiriChandanaGarimella/id-card-generator/assets/156231102/856a9380-1ba2-4866-9687-724d129117f9">

