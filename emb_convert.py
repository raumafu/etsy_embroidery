from convert_functions import *

input_folder = r"C:\Users\Rau\Desktop\emb_prep"
output_folder = r"C:\Users\Rau\Desktop\emb_prep"
input_file = r"C:\Users\Rau\Desktop\emb_prep\input.pes"
output_file = r"C:\Users\Rau\Desktop\emb_prep\scaled_out.pes"
emb_extension_write = ["dst","exp", "jef", "pes", "vp3", "xxx", "emb"]
emb_extension_read = ["dst","exp", "hus", "jef", "pes", "vp3", "xxx", "dgt", "sew", "pcs", "pcm", "csd", "pec", "shv", "vip", "art", "emb"]
hoop_center = (240, 240)
scale_factors = [0.7, 0.8, 0.9, 1,2]
pattern = pyembroidery.read(input_file)








