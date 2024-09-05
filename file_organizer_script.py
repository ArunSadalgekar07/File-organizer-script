import os
import shutil

# Specify the folder you want to organize
folder_path = input("Enter the path of the folder you want to organize: ")

# Check if the folder exists
if not os.path.exists(folder_path):
    print("The folder does not exist.")
    exit()

# Dictionary to map file extensions to folder names
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv'],
    'Audio': ['.mp3', '.wav', '.ogg', '.aac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Programs': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
}

# Function to create directories if they don't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Organize files by extension
def organize_files():
    for filename in os.listdir(folder_path):
        # Get full file path
        file_path = os.path.join(folder_path, filename)

        # Ignore directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)

        # Find the appropriate folder
        moved = False
        for folder, extensions in file_types.items():
            if file_extension.lower() in extensions:
                target_folder = os.path.join(folder_path, folder)
                create_directory(target_folder)
                shutil.move(file_path, target_folder)
                moved = True
                print(f"Moved: {filename} --> {target_folder}")
                break
        
        # If file type not found, move to "Others"
        if not moved:
            others_folder = os.path.join(folder_path, 'Others')
            create_directory(others_folder)
            shutil.move(file_path, others_folder)
            print(f"Moved: {filename} --> {others_folder}")

# Run the function
organize_files()
print("File organization complete!")
