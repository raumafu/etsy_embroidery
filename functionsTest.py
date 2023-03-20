import os
import subprocess
import shutil
import stat

def iterateFilesForExtensions(target_folder):
    file_data = []

    for item in os.listdir(target_folder):
        file_path = os.path.join(target_folder, item)
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(item)
            file_data.append((file_name, file_extension))

    return file_data


def process_files(target_folder, removeUnwantedExtensions, removeExtensionFromName, delimiter):
    def delete_unwanted_extensions(file_extension, old_file_path):
        if os.path.isfile(old_file_path):
            #print(f"Deleting file: {file_name}{file_extension}")  # Print the file name
            os.remove(old_file_path)  # Delete the file

    for file_name, file_extension in iterateFilesForExtensions(target_folder):
        old_file_path = os.path.join(target_folder, f"{file_name}{file_extension}")
        
        # Convert file_extension to lowercase for case insensitive comparison
        file_extension_lower = file_extension.lower()

        # If the file extension is in the removeUnwantedExtensions list
        if file_extension_lower in [ext.lower() for ext in removeUnwantedExtensions]:
            delete_unwanted_extensions(file_extension, old_file_path)

        # If the file extension is in the removeExtensionFromName list
        elif file_extension_lower in [ext.lower() for ext in removeExtensionFromName]:
            new_file_path = os.path.join(target_folder, f"{file_name}{delimiter}")
            os.rename(old_file_path, new_file_path)
            #print(f"Renaming file: {file_name}{file_extension} to {file_name}{delimiter}")
            
        # If the file extension is not in removeUnwantedExtensions or removeExtensionFromName
        else:
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            new_file_path = os.path.join(target_folder, f"{file_name}{file_extension}")
            shutil.move(old_file_path, new_file_path)
            #print(f"Moving file: {file_name}{file_extension} to {target_folder}")


def remove_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            if not os.listdir(dir_path):
                try:
                    # Modify folder permissions
                    os.chmod(dir_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

                    # Remove folder
                    os.rmdir(dir_path)
                    #print(f"Removed empty folder: {dir_path}")
                except PermissionError:
                    print(f"Warning: Access is denied for folder: {dir_path}")

                    
# def remove_empty_folders(path):
#     for root, dirs, files in os.walk(path, topdown=False):
#         for directory in dirs:
#             dir_path = os.path.join(root, directory)
#             if not os.listdir(dir_path):
#                 try:
#                     # Modify folder permissions
#                     os.chmod(dir_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

#                     # Remove folder
#                     os.rmdir(dir_path)
#                     #print(f"Removed empty folder: {dir_path}")
#                 except PermissionError:
#                     print(f"Warning: Access is denied for folder: {dir_path}")

#         # Move all remaining folders to the target folder
#     for root, dirs, files in os.walk(target_folder, topdown=False):
#         for folder in dirs:
#             folder_path = os.path.join(root, folder)
#             new_folder_path = os.path.join(target_folder, folder)
#             try:
#                 shutil.move(folder_path, new_folder_path)
#                 #print(f"Moved folder {folder_path} to {new_folder_path}")
#             except OSError:
#                 pass






def extract_and_remove_rar_files(target_folder, result, delimiter, seven_zip_path):
    for file_name, file_extension in result:
        file_path = os.path.join(target_folder, f"{file_name}{file_extension}")

        if delimiter in file_path:
            # Execute the 7z.exe command to extract the .rar file to the target folder
            subprocess.run(
                [seven_zip_path, "e", "-y", file_path, f"-o{target_folder}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            os.remove(file_path)  # Remove the .rar file after extraction



def delete_rar_files(target_folder, delimiter):

    for item in os.listdir(target_folder):
        file_path = os.path.join(target_folder, item)
        if os.path.isfile(file_path) and item.endswith(delimiter):
            os.remove(file_path)
            #print(f"Deleted .rar file: {file_path}")

def move_files_in_subfolders(target_folder):
    while True:
        remove_empty_folders(target_folder)
        subfolders = [f.path for f in os.scandir(target_folder) if f.is_dir()]
        if not subfolders:
            break
        for sub in subfolders:
            for f in os.listdir(sub):
                src = os.path.join(sub, f)
                dst = os.path.join(target_folder, f)
                if os.path.exists(dst):
                    file_name, file_extension = os.path.splitext(f)
                    i = 1
                    while True:
                        new_file_name = f"{file_name} ({i}){file_extension}"
                        new_dst = os.path.join(target_folder, new_file_name)
                        if not os.path.exists(new_dst):
                            dst = new_dst
                            break
                        i += 1
                shutil.move(src, dst)