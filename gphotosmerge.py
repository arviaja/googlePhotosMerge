import os
import shutil
import sys

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

def main():
    # Default to current working directory if no path provided
    source_directory = os.getcwd() if len(sys.argv) < 2 else sys.argv[1]
    target_directory = os.path.join(source_directory, 'merged_images') if len(sys.argv) < 3 else sys.argv[2]

    os.makedirs(target_directory, exist_ok=True)

    remove_json_files(source_directory)
    merge_folders(source_directory, target_directory)

if __name__ == '__main__':
    main()
