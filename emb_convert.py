import os
import shutil
import pyembroidery

input_folder = r"C:\Users\Rau\Desktop\emb_prep"
output_folder = r"C:\Users\Rau\Desktop\emb_prep\output_files"
input_file = r"C:\Users\Rau\Desktop\emb_prep\Máquina de Costura .xxx"
output_file = r"C:\Users\Rau\Desktop\emb_prep\output_files\Máquina de Costura .pes"
emb_extension_read = ["dst","exp", "jef", "pes", "vp3", "xxx", "emb"]
emb_extension_write = ["dst","exp", "hus", "jef", "pes", "vp3", "xxx", "dgt", "sew", "pcs", "pcm", "csd", "pec", "shv", "vip", "art", "emb"]


#Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


pyembroidery.convert(input_file, output_file)