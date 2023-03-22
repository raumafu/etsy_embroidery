from convert_functions import *


input_folder = r"C:\Users\Rau\Desktop\emb_prep"
output_folder = r"C:\Users\Rau\Desktop\emb_prep"
input_file = r"C:\Users\Rau\Desktop\emb_prep\input.xxx"
output_file = r"C:\Users\Rau\Desktop\emb_prep\scaled_out.pes"
emb_extension_write = ["dst","exp", "jef", "pes", "vp3", "xxx", "emb"]
emb_extension_read = ["dst","exp", "hus", "jef", "pes", "vp3", "xxx", "dgt", "sew", "pcs", "pcm", "csd", "pec", "shv", "vip", "art", "emb"]
hoop_center = (240, 240)
pattern = pyembroidery.read(input_file)
# Define scale factors
scale_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

input_file = r"C:\Users\Rau\Desktop\emb_prep\input.xxx"
output_folder = r"C:\Users\Rau\Desktop\emb_prep\scaled"


# Get the original size
width, height = get_size(input_file)
print(f"Original size: {width} x {height}")



# Resize and save all scaled files
for scale_factor in scale_factors:
    center_embroidery_pattern(input_file, pattern, hoop_center)
    resize_pattern(input_file, output_folder, scale_factor)