# File Organizer by Type

A Python script that automatically organizes files in a specified directory into categorized folders based on file types. This can help you keep your workspace clean and easy to navigate.

## Features

- Organizes files into folders like:
  - `Images`: `.jpg`, `.jpeg`, `.png`, `.gif`, etc.
  - `Documents`: `.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx`, etc.
  - `Audio`: `.mp3`, `.wav`, `.ogg`, etc.
  - `Videos`: `.mp4`, `.avi`, `.mkv`, etc.
  - `Archives`: `.zip`, `.rar`, `.tar`, etc.
  - `Programs`: `.py`, `.js`, `.html`, etc.
  - `Others`: Any unrecognized file types.
- Automatically creates folders if they do not already exist.
- Moves files into the respective folders, keeping your directory organized.

## Requirements

- Python (above 3.0)
- `shutil` (Standard Python library)
- `os` (Standard Python library)

## How to Use

1. **Clone this repository** to your local machine:

    ```bash
    git clone https://github.com/ArunSadalgekar07/File-organizer-script.git
    ```

2. **Navigate** to the project directory:

    ```bash
    cd file-organizer
    ```

3. **Run the script**:

    ```bash
    python file_organizer_script.py
    ```

4. **Enter the path of the folder** you want to organize when prompted. For example:

    ```bash
    Enter the path of the folder you want to organize: /Users/yourname/Downloads
    ```

5. The script will automatically organize your files into folders based on their type.

## Customization

- You can add or modify file types and categories by editing the `file_types` dictionary in the `file_organizer.py` file.
- The script can also be extended to sort files by other criteria like file size or date.

## Example

After running the script on a folder with various files, it will create subfolders like this:

```
Downloads/
│
├── Images/
│   ├── photo1.jpg
│   └── graphic.png
│
├── Documents/
│   ├── report.pdf
│   └── presentation.pptx
│
├── Audio/
│   └── song.mp3
│
├── Videos/
│   └── movie.mp4
│
├── Archives/
│   └── backup.zip
│
├── Programs/
│   └── script.py
│
└── Others/
    └── unknownfile.xyz
```
