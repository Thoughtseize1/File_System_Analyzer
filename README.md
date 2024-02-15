

# File System Insight Tool 🔗[Project page on PyPI](https://test.pypi.org/project/File-System-Analyzer/)
A command-line tool that analyzes and reports on the file system structure and usage on a Linux/Widows system.

## Description

File System Insight Tool is a tool for analyzing the file system. It provides detailed information about the content of a specified folder, categorizing files by types and sizes.

## Features

 - Analysis of folder content and its subfolders.
 - Categorize files by types, such as text files, images, video files, etc., based on their extensions.
 - Сalculate and display the total size for each file type category.
 - Detection of large files with the ability to set a custom size threshold.
 - Display files with unusual permissions, such as world-writable or read-only.   
 - Efficient error handling for scenarios like inaccessible directories
 - Change the current working directory using the ```cd``` command, and move one level up in the directory hierarchy using the```..``` command.

## Requirements

- Python 3.x
- Access to the file system for analyzing folders

## Installation

You can install an application directly on your system or in a virtual environment by running the command in CMD.
```
pip install -i https://test.pypi.org/simple/ File-System-Analyzer
```

🚩After installing, you can use the command ```file-analyzer``` in CMD to access the File System Insight Tool.

### 🎞[The application is demonstrated in a YouTube video.](https://youtu.be/uCHoidUI-ao)

## Avaliable commands
| Command   | Description                                               | Example                                      |
|-----------|-----------------------------------------------------------|----------------------------------------------|
| help      | Display command help                                      | help                                         |
| bye       | Say goodbye                                               | bye                                          |
| exit      | Exit the program                                          | exit                                         |
| analyze   | Analyze the contents of a folder. The current folder will be analyzed if the command is called without parameters. | analyze OR analyze D:\Torrents               |
| goto      | Set the current working folder based on the provided arguments. | goto <folder_path>                         |
| dirs      | Display the current folder path and available subfolders. | dirs                                         |
| large     | Display the largest files in the current folder            | large                                        |
| setsize   | Set the threshold size for identifying large files (in MB)| setsize <size>                               |
| show      | Display the contents of the current folder or the specified folder path. | show OR show <folder_path>                |
| cd        | Change the current working directory to the specified path.| cd <directory> OR cd venv                   |
| ..        | Move up one level in the directory structure               | ..                                           |
| stats     | Show statistics about file types and sizes                | stats                                        |
| permissions| Show files with unusual permissions (World-writable or Read-only) | permissions                         |
| ignore    | Display the list of folders currently marked to be ignored during analysis. Ignored folders will be excluded from the analysis process. | ignore                    |
| addignore | Add a folder to the list of ignored folders. Folders in this list will not be analyzed in subsequent operations. | addignore                       |
