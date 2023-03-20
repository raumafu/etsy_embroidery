from functionsTest import *
#import Levenshtein as lev


# Define the target folder path
target_folder = r"C:\Users\Rau\Desktop\emb_files"

#target_folder = r"C:\Users\Rau\Desktop\Compressed"
# List of extensions to be removed from the file name
removeExtensionFromName = [".doar", ".edr", ".ev", ".mb", ".TB", ".wcn", ".EDR"]
# List of unwanted extensions to be deleted
removeUnwantedExtensions = [".ini", ".jfif", ".lha", ".otf", ".ttf", ".BMP", ".jpg", ".db", ".jpeg"]
# File extension delimiter for .rar files
delimiter = ".rar"
# Path to the 7z.exe executable
seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
# List of PES .rar file names to check


process_files(target_folder, removeUnwantedExtensions, removeExtensionFromName, delimiter)


# def group_similar_files(target_folder, similarity_threshold):
#     # Create a dictionary to store the file groups
#     file_groups = {}

#     # Get a list of files in the target folder
#     file_list = os.listdir(target_folder)

#     # Loop through each file in the target folder
#     for file_name in file_list:
#         # Create a flag variable to track if the file has been added to a group
#         added_to_group = False

#         # Loop through each group in the file_groups dictionary
#         for group_name, group_files in file_groups.items():
#             # Loop through each file in the group
#             for group_file in group_files:
#                 # Calculate the similarity between the two file names using the Levenshtein distance algorithm
#                 similarity_score = lev.distance(file_name, group_file)

#                 # If the similarity score is above the threshold, add the file to the group
#                 if similarity_score <= similarity_threshold:
#                     group_files.append(file_name)
#                     added_to_group = True
#                     print(f"Added file {file_name} to group {group_name}")
#                     break

#             # If the file has been added to a group, break out of the loop
#             if added_to_group:
#                 break

#         # If the file has not been added to a group, create a new group with the file as the first item
#         if not added_to_group:
#             group_name = os.path.splitext(file_name)[0]
#             file_groups[group_name] = [file_name]
#             print(f"Created new group {group_name} with file {file_name}")

#     # Loop through each group in the file_groups dictionary and move the files to a new folder
#     for group_name, group_files in file_groups.items():
#         group_folder = os.path.join(target_folder, group_name)
#         os.makedirs(group_folder, exist_ok=True)
#         for group_file in group_files:
#             src_path = os.path.join(target_folder, group_file)
#             dst_path = os.path.join(group_folder, group_file)
#             shutil.move(src_path, dst_path)
#             print(f"Moved file {group_file} to group folder {group_name}")

# # Example usage
# group_similar_files(target_folder, 5)
