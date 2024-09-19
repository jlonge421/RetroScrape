# This script appends extensions to files based on their MIME type.
# Use this script if you have files with no extensions.

import os
import mimetypes
import shutil
import magic  # External library for better MIME type detection

# Function to detect the MIME type and suggest an extension
def get_extension_from_mime(filepath):
    # First, try to guess the MIME type using the python 'mimetypes' module
    mime_type, _ = mimetypes.guess_type(filepath)
    
    # External library 'python-magic' for more accurate detection
    if not mime_type:
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(filepath)
    
    # Dictionary to handle cases where mimetypes don't map directly to extensions
    mime_to_extension = {
        "text/html": ".html",
        "text/css": ".css",
        "application/javascript": ".js",
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/svg+xml": ".svg",
        "application/pdf": ".pdf",
        "application/zip": ".zip"
    }

    # If a custom mime to extension mapping exists, return it
    if mime_type in mime_to_extension:
        return mime_to_extension[mime_type]
    
    # If it's a known MIME type, return the appropriate extension
    if mime_type:
        ext = mimetypes.guess_extension(mime_type)
        return ext
    return None

# Function to add the correct extension if necessary
def add_extension_based_on_mime(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(subdir, file)
            current_extension = os.path.splitext(filepath)[1]
            
            # Get suggested extension from MIME type
            suggested_extension = get_extension_from_mime(filepath)

            # Debug output: Print MIME type and file path
            print(f"Processing file: {filepath} - MIME type: {suggested_extension}")

            # Only proceed if the file lacks an extension or has a wrong one
            if suggested_extension and current_extension != suggested_extension:
                new_filepath = filepath + suggested_extension

                # Rename the file with the correct extension
                shutil.move(filepath, new_filepath)
                print(f"Renamed: {filepath} -> {new_filepath}")
            else:
                print(f"Skipped: {filepath}")

# Set the root directory where your files are located
root_directory = r'C:\Users\xyz\Desktop\Repos\LTGcoaches\wget1\web.archive.org\web'

# Run the function to add extensions based on MIME type
add_extension_based_on_mime(root_directory)
