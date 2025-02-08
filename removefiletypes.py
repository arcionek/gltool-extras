import os
import shutil

# Path to the "anim" folder (root folder)
base_path = os.getcwd()  # Assumes the script is placed in the "anim" folder
output_folder = os.path.join(base_path, 'output')  # Path to the 'output' folder

# Create 'output' folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created 'output' folder: {output_folder}")

# Loop through all subfolders and files in the "anim" folder
for root, dirs, files in os.walk(base_path, topdown=False):  # Process subfolders first
    # Skip the 'output' folder to avoid processing it
    if root == output_folder:
        continue
    
    # Remove .tex and .bin files
    for file in files:
        if file.endswith(('.tex', '.bin')):
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    
    # Process each subfolder
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        new_dir_path = dir_path  # Default new_dir_path is the original folder path
        
        # Remove .zip from folder names, if it exists
        if dir.endswith('.zip'):
            new_dir_name = dir[:-4]  # Remove the ".zip" suffix
            new_dir_path = os.path.join(root, new_dir_name)
            try:
                os.rename(dir_path, new_dir_path)
                print(f"Renamed folder: {dir_path} -> {new_dir_path}")
            except Exception as e:
                print(f"Error renaming folder {dir_path}: {e}")
        
        # Process .png files inside the folder
        folder_name = os.path.basename(new_dir_path)  # Get the name of the folder (without path)
        for file in os.listdir(new_dir_path):  # List files inside the folder
            if file.endswith('.png') and file.startswith('atlas'):
                # Build the new file name (using the folder name)
                file_path = os.path.join(new_dir_path, file)
                new_file_name = f"{folder_name}-{file[6:]}"  # Rename atlas-<n>.png to foldername-<n>.png
                new_file_path = os.path.join(output_folder, new_file_name)  # Move to the output folder
                
                try:
                    # Rename and move the file to the 'output' folder
                    shutil.move(file_path, new_file_path)
                    print(f"Moved and renamed: {file_path} -> {new_file_path}")
                except Exception as e:
                    print(f"Error moving/renaming file {file_path}: {e}")
        
        # Remove the folder after moving the PNG files
        if not os.listdir(new_dir_path):  # Check if the folder is now empty
            try:
                os.rmdir(new_dir_path)
                print(f"Removed empty folder: {new_dir_path}")
            except Exception as e:
                print(f"Error removing folder {new_dir_path}: {e}")

print("Task completed.")
