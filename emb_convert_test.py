from convert_functions_test import *  # Import all functions from the convert_functions module

# Variables
source_folder = r"C:\Users\Rau\Desktop\emb_prep"  # Input folder for the embroidery files

files = os.listdir(source_folder)


# Loop over each file in the source folder
for file in files:
    input_file = os.path.join(source_folder, file)
    file_name, _ = os.path.splitext(file)  # Get the file name without extension

    # Output folder for the scaled embroidery files
    output_folder = rf"C:\Users\Rau\Desktop\emb_prep\{file_name}"
    parent_folder = os.path.dirname(output_folder)
    zip_name = os.path.join(parent_folder, f"{file_name}.zip")

    # Start Timer to measure the execution time
    start_time = time.time()

    # Loop over each extension and scale the input file for each extension
    for extension in extensions:
        # Call the resize_pattern function for each scale factor
        for scale_factor in scale_factors:
            resize_pattern(input_file, output_folder, scale_factor, extension, hoop_center)

        # Call the zip_folder function after the conversion loop
    zip_folder(parent_folder, output_folder, zip_name, zip_exe_path)


# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")