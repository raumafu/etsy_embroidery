import os
import shutil
import pyembroidery

def makeDir(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


def move_design_to_origin(design):
    min_x, min_y = float('inf'), float('inf')

    for stitch in design.stitches:
        x, y, cmd = stitch
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    for i, stitch in enumerate(design.stitches):
        x, y, cmd = stitch
        design.stitches[i] = (x - min_x, y - min_y, cmd)