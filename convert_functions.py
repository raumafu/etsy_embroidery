import os
import shutil
import pyembroidery

def makeDir(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder
