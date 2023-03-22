from convert_functions import *

input_folder = r"C:\Users\Rau\Desktop\emb_prep"
output_folder = r"C:\Users\Rau\Desktop\emb_prep\output_files"
input_file = r"C:\Users\Rau\Desktop\emb_prep\Máquina de Costura .xxx"
output_file = r"C:\Users\Rau\Desktop\emb_prep\output_files\Máquina de Costura .pes"
emb_extension_write = ["dst","exp", "jef", "pes", "vp3", "xxx", "emb"]
emb_extension_read = ["dst","exp", "hus", "jef", "pes", "vp3", "xxx", "dgt", "sew", "pcs", "pcm", "csd", "pec", "shv", "vip", "art", "emb"]




input_file = "input.pes"
output_file = "centered_output.pes"
hoop_center = (240, 240)

center_embroidery_file(input_file, output_file, hoop_center)
