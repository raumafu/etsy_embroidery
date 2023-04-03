from convert_functions import *  # Import all functions from the convert_functions module
import threading
import time

# Variables
input_file = r"C:\Users\Rau\Desktop\emb_prep\input.pes"  # Input embroidery file path
output_folder = r"C:\Users\Rau\Desktop\emb_prep\scaled"  # Output folder for the scaled embroidery files
hoop_center = (350, 350)  # Center coordinates of the embroidery hoop
# pattern = pyembroidery.read(input_file)
# Define scale factors to apply on the embroidery design
scale_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

# Start Timer to measure the execution time
start_time = time.time()

# Create a list to hold the threads
threads = []

# Create a thread for each scale factor
for scale_factor in scale_factors:
    # Create a new thread for this scale factor, which will execute the resize_pattern function
    thread = threading.Thread(target=resize_pattern, args=(input_file, output_folder, scale_factor))
    # Add the thread to the list of threads
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# Wait for all the threads to finish
for thread in threads:
    thread.join()

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Add google image recognition
# Add multiple file type exports
# Add ui for selecting input file and output folder
# Add Etsy API integration
# Creating output folder names based on input name in the ui