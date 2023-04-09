from convert_functions_test import *  # Import all functions from the convert_functions module
# Start Timer to measure the execution time
start_time = time.time()


# Loop over each file in the source folder
for file in files:
    input_file = os.path.join(source_folder, file)
    file_name, _ = os.path.splitext(file)

    # Output folder for the scaled embroidery files
    output_folder = rf"C:\Users\Rau\Desktop\emb_prep\{file_name}"
    parent_folder = os.path.dirname(output_folder)
    zip_name = os.path.join(parent_folder, f"{file_name}.zip")

    process_input_file(input_file, output_folder, extensions, scale_factors, hoop_center)

    zip_folder(parent_folder, output_folder, zip_name, zip_exe_path)
    print(f"Zipped {file_name} to {zip_name}")

    dest_work_files_folder = os.path.join(work_files_folder, file_name)
    dest_to_be_uploaded = os.path.join(to_be_uploaded_folder, f"{file_name}.zip")
    dest_to_get_images = os.path.join(to_get_images_folder, file)

    move_files(output_folder, dest_work_files_folder)
    move_files(zip_name, dest_to_be_uploaded)
    move_files(input_file, dest_to_get_images)

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time for {file_name}: {elapsed_time:.2f} seconds")

