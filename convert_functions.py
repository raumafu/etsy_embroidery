import os
import pyembroidery
import subprocess
import math

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


def scale_and_save(input_file, output_folder, scale_factor):
    pattern = pyembroidery.read(input_file)
    matrix = pyembroidery.EmbMatrix()
    matrix.post_scale(scale_factor, scale_factor)
    pattern.transform(matrix)

    min_x, min_y, max_x, max_y = pattern.extents()
    width = math.ceil((max_x - min_x) / 10)
    height = math.ceil((max_y - min_y) / 10)

    output_file = output_folder + f"\\bear_W{width}_H{height}.pes"
    pyembroidery.write(pattern, output_file)

    print(f"File saved to: {output_file}")


    for scale_factor in scale_factors:
        center_embroidery_pattern(input_file, pattern, hoop_center)
        scale_and_save(input_file, output_folder, scale_factor)