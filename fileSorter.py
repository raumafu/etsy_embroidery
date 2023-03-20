from functionsTest import *

# Define the target folder path
target_folder = r"C:\Users\Rau\Desktop\emb_files"
# target_folder = r"C:\Users\Rau\Desktop\Compressed"
# List of extensions to be removed from the file name
removeExtensionFromName = [".doar", ".edr", ".ev", ".mb", ".TB", ".wcn", ".EDR", ".bak"]
# List of unwanted extensions to be deleted
removeUnwantedExtensions = [".tbf",".phc",".png",".ini",".inf", ".jef+", ".DS_Store", ".rgb", ".jfif",".ap", ".lha", ".otf", ".ttf", ".BMP", ".jpg", ".db", ".jpeg", ".pdf", "._aplique", "._chaveiros", ".bmc", ".cdr", ".cnd", ".csd", ".ct0", ".dgf"]
# File extension delimiter for .rar files
delimiter = ".rar"
# Path to the 7z.exe executable
seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
# List of PES .rar file names to check

#move_files_in_subfolders(target_folder)

# Get the list of files with their names and extensions in the target folder
result = iterateFilesForExtensions(target_folder)
# Process the files (delete unwanted files, rename others)
process_files(target_folder, removeUnwantedExtensions, removeExtensionFromName, delimiter)

# Get the updated list of files after processing
result = iterateFilesForExtensions(target_folder)

# Extract and remove .rar files in the target folder
extract_and_remove_rar_files(target_folder, result, delimiter, seven_zip_path)

# Delete all remaining .rar files in the target folder
delete_rar_files(target_folder, delimiter)

# Update the result variable with the new list of files
result = iterateFilesForExtensions(target_folder)

# Check for Leftovers
process_files(target_folder, removeUnwantedExtensions, removeExtensionFromName, delimiter)

# Remove empty folders in the target folder
remove_empty_folders(target_folder)

# Move all created subfolders to the target folder
remove_empty_folders(target_folder)

# Delete all remaining .rar files in the target folder (add this line)
delete_rar_files(target_folder, delimiter)

# Update the result variable with the new list of files
result = iterateFilesForExtensions(target_folder)
