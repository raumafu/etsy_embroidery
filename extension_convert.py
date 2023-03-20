from extension_convert_functions import *
import pyembroidery
from pyembroidery import EmbPattern, EmbThread


input_folder = r"C:\Users\Rau\Desktop\emb_prep"
output_folder = r"C:\Users\Rau\Desktop\emb_prep\output_files"
input_file = r"C:\Users\Rau\Desktop\emb_prep\Máquina de Costura.pes"
output_file = r"C:\Users\Rau\Desktop\emb_prep\output_files\tested_switched4.pes"
emb_extension_write = ["dst","exp", "jef", "pes", "vp3", "xxx", "emb"]
emb_extension_read = ["dst","exp", "hus", "jef", "pes", "vp3", "xxx", "dgt", "sew", "pcs", "pcm", "csd", "pec", "shv", "vip", "art", "emb"]




design = pyembroidery.read(input_file)

# Move the design to the origin (0, 0)
move_design_to_origin(design)

# Save the modified design
pyembroidery.write(design, output_file)



