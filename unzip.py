import zipfile
import os

# Path to the uploaded zip file
zip_file_path = '/mnt/data/1st-20241110T182432Z-001.zip'
# Directory to extract the contents
extracted_dir = '/mnt/data/pizza_delivery_app/'

# Extracting the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

# Listing the contents to understand the structure
extracted_files = []
for root, dirs, files in os.walk(extracted_dir):
    for file in files:
        extracted_files.append(os.path.join(root, file))

extracted_files
