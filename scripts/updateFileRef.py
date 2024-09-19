import os
import re

# Function to remove the versioning part from file references in an HTML, CSS, or JS file
def clean_up_html_references(file_path):
    # Open the file for reading
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Log the file being processed
    print(f"Processing file: {file_path}")
    
    # Regex pattern to match file references that contain '@' or '?' in src, href, or link attributes
    # This matches any characters before a valid file extension (like .js, .css) followed by @... or ?...
    cleaned_content = re.sub(r'(\.[a-z]{2,4})([@?][^"\']*)', r'\1', content)

    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    print(f"Cleaned references in: {file_path}")

# Function to recursively process all HTML, CSS, and JS files in a directory
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
