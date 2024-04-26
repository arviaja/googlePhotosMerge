import os
import shutil
import zipfile

def unzip_files(zip_paths, extract_path):
    """Unzip files to the specified directory."""
    for zip_path in zip_paths:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

def remove_json_files(directory):
    """Remove all JSON files in the directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                os.remove(os.path.join(root, file))

def merge_folders(source_dir, target_dir):
    """Recursively move files from source to target, rename duplicates."""
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if not file.endswith('.json'):
                src_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, file)
                # Check if file exists and rename if necessary
                copy_num = 1
                file_name, file_extension = os.path.splitext(file)
                while os.path.exists(target_file):
                    target_file = os.path.join(target_dir, f"{file_name}_{copy_num}{file_extension}")
                    copy_num += 1
                shutil.move(src_file, target_file)

# Example usage:
zip_files = ['path/to/your/first.zip', 'path/to/your/second.zip']  # List your zip file paths here
extract_path = 'path/to/extracted'  # Path where zip files will be extracted
target_directory = 'path/to/merged_images'  # All images will be moved here

os.makedirs(extract_path, exist_ok=True)
os.makedirs(target_directory, exist_ok=True)

unzip_files(zip_files, extract_path)
remove_json_files(extract_path)
merge_folders(extract_path, target_directory)
