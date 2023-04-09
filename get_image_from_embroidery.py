import pyembroidery
import os

# Read embroidery file
input_file = r"C:\Users\Rau\Desktop\emb_prep\BeachBallBuddies.jef"  # Input embroidery file path
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

# convert_embroidery_to_image(input_file, output_file)


def edit_image(input_image_path, output_image_path):
    # Open the original image
    image = Image.open(input_image_path)

    # Create a white background with the recommended Etsy resolution
    white_background = Image.new("RGB", (2000, 2000), "white")

    # Calculate the position to center the original image on the white background
    position = (
        (white_background.width - image.width) // 2,
        (white_background.height - image.height) // 2
    )

    # Paste the original image onto the white background
    white_background.paste(image, position)

    # Save the edited image
    white_background.save(output_image_path)

# Usage example
input_image_path = r"C:\Users\Rau\Desktop\emb_prep\image.png"
output_image_path = r"C:\Users\Rau\Desktop\emb_prep\imageEdited.png"
edit_image(input_image_path, output_image_path)