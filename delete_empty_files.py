# Import necessary libraries
import os
import tkinter as tk
from tkinter import filedialog


# Define the function to delete empty folders
def delete_empty_folders(start_path, output_label):
    # Initialize a counter for deleted folders
    deleted_folders_count = 0
    # Walk through the folder structure
    for root, dirs, files in os.walk(start_path, topdown=False):
        # Loop through each directory in the current root
        for dir in dirs:
            # Construct the full path of the directory
            dir_path = os.path.join(root, dir)
            # Check if the directory is empty
            if not os.listdir(dir_path):
                # Update the output label with the deleted folder path
                output_label["text"] += f"Deleting empty folder: {dir_path}\n"
                # Remove the empty directory
                os.rmdir(dir_path)
                # Increment the deleted folders counter
                deleted_folders_count += 1
    # Update the output label with the total number of deleted folders
    output_label[
        "text"
    ] += f"Total number of deleted empty folders: {deleted_folders_count}\n"


# Define the callback function for the browse button
def browse_button_callback(output_label):
    # Open a folder selection dialog
    folder_path = filedialog.askdirectory()
    # Check if a folder has been selected
    if folder_path:
        # Call the delete_empty_folders function with the selected folder path
        delete_empty_folders(folder_path, output_label)


# Define the function to create the UI
def create_ui():
    # Create the main window
    root = tk.Tk()
    # Set the window title
    root.title("Delete Empty Folders")

    # Create a label to display the output
    output_label = tk.Label(root, justify=tk.LEFT, anchor=tk.NW)
    # Pack the label with proper settings to fill the window
    output_label.pack(fill=tk.BOTH, expand=True)

    # Create a browse button with a callback function
    browse_button = tk.Button(
        root, text="Browse", command=lambda: browse_button_callback(output_label)
    )
    # Pack the browse button at the bottom of the window
    browse_button.pack(side=tk.BOTTOM)

    # Run the main event loop of the UI
    root.mainloop()


# Check if the script is being run as the main module
if __name__ == "__main__":
    # Call the create_ui function to create and run the UI
    create_ui()
