import os
import pyembroidery
import math
import time
import threading


def makeDir(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


def center_embroidery_pattern(input_file, pattern, hoop_center):
    pattern = pyembroidery.read(input_file)
    hoop_center = (240, 240)
    min_x, min_y, max_x, max_y = pattern.extents()
    design_center = ((min_x + max_x) / 2, (min_y + max_y) / 2)
    translation = (hoop_center[0] - design_center[0], hoop_center[1] - design_center[1])

    for stitch in pattern.stitches:
        stitch[0] += translation[0]
        stitch[1] += translation[1]

    return pattern



def get_size(input_file):
    pattern = pyembroidery.read(input_file)
    min_x, min_y, max_x, max_y = pattern.extents()
    width = max_x - min_x
    height = max_y - min_y
    return width, height

def resize_pattern(input_file, output_folder, scale_factor):
    pattern = pyembroidery.read(input_file)
    matrix = pyembroidery.EmbMatrix()
    matrix.post_scale(scale_factor, scale_factor)
    pattern.transform(matrix)

    # Create output folder if it does not exist
    makeDir(output_folder)

    # Save the resized embroidery file
    width, height = get_size(input_file)
    new_width = math.ceil(width * scale_factor)
    new_height = math.ceil(height * scale_factor)
    output_file = os.path.join(output_folder, f"scaled_{new_width / 100 }cm x {new_height / 100 }cm .pes")
    pyembroidery.write(pattern, output_file)

    # Print the size of the resized embroidery file
    # print(f"Resized {scale_factor}x: {new_width} x {new_height}")

