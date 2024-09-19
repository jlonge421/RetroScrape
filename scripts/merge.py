# This script merges all unique files from multiple folders into one folder,
# without messing up the folder structure

import os
import shutil
from filecmp import cmp

# Function to merge unique files from multiple snapshot directories while preserving folder structure
def merge_unique_files(snapshots_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Dictionary to track unique files (based on their relative paths)
    unique_files = {}

    # Walk through all snapshot directories
    for subdir, dirs, files in os.walk(snapshots_dir):
        # We are only interested in the www.ltgcoaches.com directory inside each snapshot
        if "www.ltgcoaches.com" in subdir:
            for file in files:
                file_path = os.path.join(subdir, file)
                
                # Calculate the relative path starting from the www.ltgcoaches.com folder
                relative_path = os.path.relpath(file_path, os.path.join(subdir.split("www.ltgcoaches.com")[0], "www.ltgcoaches.com"))
                dest_path = os.path.join(output_dir, relative_path)
                dest_dir = os.path.dirname(dest_path)

                # Create destination directory if it does not exist
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                # Check if the file with this relative path is already recorded
                if relative_path in unique_files:
                    # If a file with the same relative path exists, compare them
                    existing_file_path = unique_files[relative_path]
                    if not cmp(file_path, existing_file_path, shallow=False):
                        print(f"Duplicate but different file found: {file_path} vs {existing_file_path}")
                    else:
                        print(f"Duplicate identical file skipped: {file_path}")
                else:
                    # If the file is unique, copy it to the destination
                    shutil.copy2(file_path, dest_path)  # Copy the file to the output directory
                    unique_files[relative_path] = file_path  # Track the file's relative path
                    print(f"File copied: {file_path} -> {dest_path}")

# Set the root directory where all snapshots are located (which contain www.ltgcoaches.com folders)
snapshots_directory = r'C:/Users/xyz/Desktop/Repos/LTGcoaches/wget2/web.archive.org/web/'

# Set the output directory where the merged unique files will be stored
output_directory = r'C:/Users/xyz/Desktop/Repos/LTGcoaches/complete_site/'

# Run the function to merge unique files while preserving folder structure
merge_unique_files(snapshots_directory, output_directory)
