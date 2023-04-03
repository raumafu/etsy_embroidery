from convert_functions_test import *  # Import all functions from the convert_functions module

# Variables
input_file = r"C:\Users\Rau\Desktop\emb_prep\input.pes"  # Input embroidery file path
output_folder = r"C:\Users\Rau\Desktop\emb_prep\scaled"  # Output folder for the scaled embroidery files
hoop_center = (350, 350)  # Center coordinates of the embroidery hoop
extensions = ['pes', 'dst', 'jef', 'exp', 'vp3', 'xxx']

# Define scale factors to apply on the embroidery design
scale_factors = [0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

# Start Timer to measure the execution time
start_time = time.time()

# Loop over each extension and scale the input file for each extension
for extension in extensions:
    # Call the resize_pattern function for each scale factor
    for scale_factor in scale_factors:
        resize_pattern(input_file, output_folder, scale_factor, extension, hoop_center)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")