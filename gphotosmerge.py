import os
import shutil

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
source_directory = 'path/to/extracted'  # Path where your photos are already extracted
target_directory = 'path/to/merged_images'  # All images will be moved and merged here

os.makedirs(target_directory, exist_ok=True)

remove_json_files(source_directory)
merge_folders(source_directory, target_directory)
