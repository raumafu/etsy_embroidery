import os
import pyembroidery
import math
import subprocess
import time
import shutil

#Variables
source_folder = rf"C:\Users\Rau\Desktop\emb_prep"  # Input folder for the embroidery files
work_files_folder = r"C:\Users\Rau\Desktop\work_files"
to_be_uploaded_folder = r"C:\Users\Rau\Desktop\to_be_uploaded"
to_get_images_folder = r"C:\Users\Rau\Desktop\to_get_images"
zip_exe_path = r"C:\Program Files\7-Zip\7z.exe"
extensions = ['pes', 'dst', 'jef', 'exp', 'vp3', 'xxx']
hoop_center = (350, 350)  # Center coordinates of the embroidery hoop
# Define scale factors to apply on the embroidery design
scale_factors = [0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

files = os.listdir(source_folder)
# Create necessary folders if they don't exist
os.makedirs(work_files_folder, exist_ok=True)
os.makedirs(to_be_uploaded_folder, exist_ok=True)
os.makedirs(to_get_images_folder, exist_ok=True)

def process_input_file(input_file, output_folder, extensions, scale_factors, hoop_center):
    for extension in extensions:
        for scale_factor in scale_factors:
            resize_pattern(input_file, output_folder, scale_factor, extension, hoop_center)


def move_files(src, dest):
    shutil.move(src, dest)
    print(f"Moved {src} to {dest}")




def zip_folder(parent_folder, output_folder, zip_name, zip_exe_path):
    # Check if the 7zip command-line executable is available
    try:
        subprocess.run([zip_exe_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        raise FileNotFoundError(f"{zip_exe_path} not found. Make sure the path is correct and 7zip is installed.")

    # Compress the parent folder using 7zip
    zip_command = [zip_exe_path, "a", "-tzip", zip_name, output_folder]
    subprocess.run(zip_command, cwd=parent_folder)


def makeDir(output_folder):
    path = ""
    for folder in output_folder.split(os.path.sep):
        path = os.path.join(path, folder)
        if not os.path.exists(path):
            os.mkdir(path)
    return output_folder


def convert_embroidery_to_image(input_file, output_file):
    # Read embroidery file
    pattern = pyembroidery.read(input_file)

    # Create output folder if it does not exist
    output_folder = os.path.dirname(output_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write embroidery file as PNG
    pyembroidery.write_png(pattern, output_file)


def center_embroidery_pattern(pattern, hoop_center):
    # Get the design bounds
    min_x, min_y, max_x, max_y = pattern.bounds()
    
    # Get the design center and the translation needed to center it in the hoop
    design_center = ((min_x + max_x) / 2, (min_y + max_y) / 2)
    translation = (hoop_center[0] - design_center[0], hoop_center[1] - design_center[1])
    
    # Apply the translation to all the stitches
    for stitch in pattern.stitches:
        stitch[0] += translation[0]
        stitch[1] += translation[1]
        
    return pattern



def get_size(input_file):
    pattern = pyembroidery.read(input_file)
    min_x, min_y, max_x, max_y = pattern.extents()
    width, height = abs(max_x - min_x), abs(max_y - min_y)
    return width, height


def resize_pattern(input_file, output_folder, scale_factor, extension, hoop_center):
    pattern = pyembroidery.read(input_file)
    matrix = pyembroidery.EmbMatrix()
    matrix.post_scale(scale_factor, scale_factor)
    pattern.transform(matrix)

    # Center the embroidery pattern
    pattern = center_embroidery_pattern(pattern, hoop_center)

    # Create output folder if it does not exist
    output_extension_folder = os.path.join(output_folder, extension)
    makeDir(output_extension_folder)

    # Save the resized embroidery file
    width, height = get_size(input_file)
    new_width = math.ceil(width * scale_factor)
    new_height = math.ceil(height * scale_factor)
    new_width_inch = new_width / 254.0  # Convert millimeters to inches (1 inch = 25.4 mm)
    new_height_inch = new_height / 254.0
    output_file = os.path.join(
        output_extension_folder,
        f"{new_width / 100:.2f} cm x {new_height / 100:.2f} cm ({new_width_inch:.2f} in x {new_height_inch:.2f} in).{extension}"
    )
    pyembroidery.write(pattern, output_file)
