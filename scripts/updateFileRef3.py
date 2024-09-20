import os
import re

# Function to clean up href and src references in an HTML file
def clean_up_html_references(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Log the file being processed
    print(f"Processing file: {file_path}")

    # Step 1: Remove the domain 'http://www.ltgcoaches.com' from href and src attributes
    content = re.sub(r'http(s)?://(www\.)?ltgcoaches\.com', '', content)

    # Step 2: Remove any triple slashes left behind (http:/// becomes http://)
    content = re.sub(r'http:///+', 'http://', content)

    # Step 3: Remove any double slashes in paths (e.g., ///media/ to /media/)
    content = re.sub(r'/+', '/', content)

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
