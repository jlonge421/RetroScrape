# This script updates HTML file references
# Unlike updateFileRef.py, this script converts referenced path to files to relative file paths, 
# as opposed to pointing to archived material
# 
import os
import re
import urllib.parse

# Function to clean up href and src references in an HTML file
def clean_up_html_references(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Log the file being processed
    print(f"Processing file: {file_path}")
    
    # Step 1: Remove the `../../../20180822071315cs_/` or similar prefix
    content = re.sub(r'\.\./\.\./\.\./[0-9]+[a-z]{2,3}_/', '', content)
    
    # Step 2: Decode percent-encoded URLs (like http%253A to http://)
    # Example: http%253A/www.ltgcoaches.com becomes http://www.ltgcoaches.com
    content = re.sub(r'http%253A', 'http://', content)
    content = re.sub(r'https%253A', 'https://', content)

    # Step 3: Remove any remaining "http://" prefixes to make the URLs relative
    content = re.sub(r'http://www\.ltgcoaches\.com', '', content)

    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Cleaned references in: {file_path}")

# Function to recursively process all HTML files in a directory
def process_directory(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(subdir, file)
                clean_up_html_references(file_path)

# Set the root directory where your HTML files are located
project_directory = r'C:/Users/xyz/Desktop/Repos/LTGcoaches/complete_site/'

# Process the directory to clean up file references
process_directory(project_directory)

