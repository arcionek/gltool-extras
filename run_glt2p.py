import os
import subprocess

# Name of the scripts to run
glt2p_script = "glt2p.py"
removefiletypes_script = "removefiletypes.py"

# Get the current directory (assuming it's the "src" folder)
current_dir = os.getcwd()

# Iterate over all entries in the current directory
for folder_name in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, folder_name)

    # Check if the entry is a folder and not __pycache__
    if os.path.isdir(folder_path) and folder_name != "__pycache__":
        try:
            # Run the glt2p.py script with the folder as input
            print(f"Running {glt2p_script} with input: {folder_name}")
            subprocess.run(["python", os.path.join(current_dir, glt2p_script), folder_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while processing folder {folder_name}: {e}")

# After all glt2p.py processes finish, run removefiletypes.py
try:
    print(f"Running {removefiletypes_script} after all glt2p.py processes.")
    subprocess.run(["python", os.path.join(current_dir, removefiletypes_script)], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error while running {removefiletypes_script}: {e}")
