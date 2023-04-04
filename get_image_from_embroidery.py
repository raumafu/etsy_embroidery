import pyembroidery
import os
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.oauth2.service_account import Credentials

# Read embroidery file
input_file = r"C:\Users\Rau\Desktop\emb_prep\input.pes"  # Input embroidery file path
output_file = r"C:\Users\Rau\Desktop\emb_prep\image.png"

def convert_embroidery_to_image(input_file, output_file):
    # Read embroidery file
    pattern = pyembroidery.read(input_file)

    # Create output folder if it does not exist
    output_folder = os.path.dirname(output_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write embroidery file as PNG
    pyembroidery.write_png(pattern, output_file)

client = vision.ImageAnnotatorClient()
file_name = output_file

# Loads the image into memory
with open(file_name, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)