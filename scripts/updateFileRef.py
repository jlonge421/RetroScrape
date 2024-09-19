# This script will update the file references in HTML files
# It will find all references to filenames with '@' in them and remove '@' and any string that comes after
# Script was developed to work on archived files.

import os
import re

# Function to remove query strings from file references in an HTML file
def clean_up_html_references(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to find src or href attributes with query strings (e.g., ?abc123 after .js, .css, etc.)
    cleaned_content = re.sub(r'([a-zA-Z0-9_-]+)\.[a-z]+@[^"\']+', r'\1', content)

    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
    print(f"Processed: {file_path}")

# Function to recursively process all HTML files in a directory
def process_directory(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.css') or file.endswith('.js'):
                file_path = os.path.join(subdir, file)
                clean_up_html_references(file_path)

# Set the root directory where your HTML, CSS, and JS files are located
project_directory = r'C:/Users/xyz/Desktop/Repos/LTGcoaches/complete_site/'

# Process the directory to clean up file references
process_directory(project_directory)
