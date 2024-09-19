# This script is used to remove unneccessary appends to the file name.

import os

# Function to clean up filenames by removing the part after '@'
def clean_up_filenames(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if '@' in file:
                file_path = os.path.join(subdir, file)
                
                # Split at '@' and keep only the part before it (the original filename)
                new_file_name = file.split('@')[0]
                new_file_path = os.path.join(subdir, new_file_name)
                
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_path} -> {new_file_path}")

# Set the root directory where your files are located
root_directory = r'C:/Users/xyz/Desktop/Repos/LTGcoaches/complete_site/'

# Run the function to clean up filenames
clean_up_filenames(root_directory)
