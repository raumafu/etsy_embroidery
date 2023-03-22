import os
import shutil
import pyembroidery

def makeDir(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


def center_embroidery_file(input_file, output_file, hoop_center):
    def center_embroidery_pattern(pattern, hoop_center):
        # Calculate the design's bounding box
        min_x = min(stitch[0] for stitch in pattern.stitches)
        max_x = max(stitch[0] for stitch in pattern.stitches)
        min_y = min(stitch[1] for stitch in pattern.stitches)
        max_y = max(stitch[1] for stitch in pattern.stitches)

        # Calculate the design's center
        design_center = ((min_x + max_x) / 2, (min_y + max_y) / 2)

        # Calculate the translation required to center the design
        translation = (hoop_center[0] - design_center[0], hoop_center[1] - design_center[1])

        # Move the design to the center of the hoop
        for stitch in pattern.stitches:
            stitch[0] += translation[0]
            stitch[1] += translation[1]

    # Read the input .pes file
    pattern = pyembroidery.read(input_file)

    # Center the design within the hoop
    center_embroidery_pattern(pattern, hoop_center)

    # Save the centered design to a new .pes file
    pyembroidery.write(pattern, output_file)
