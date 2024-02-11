

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
 - Change the current working directory using the 'cd' command, and move one level up in the directory hierarchy using the '..' command.

## Requirements

- Python 3.x
- Access to the file system for analyzing folders

## Installation

You can install an application directly on your system or in a virtual environment by running the command in CMD.
```
pip install -i https://test.pypi.org/simple/ File-System-Analyzer
```

🚩After installing, you can use the command `file-analyzer` in CMD to access the File System Insight Tool.
## Avaliable commands

| Command   | Description                                               | Example                                      |
|-----------|-----------------------------------------------------------|----------------------------------------------|
| help      | Display command help                                      | help                                         |
| hello/hi    | Display a greeting message                              | hello                                        |
| bye/exit  | End the program                                           | bye or exit                                  |
| analyze   | Analyze the specified folder                              | analyze OR analyze D:\Torrents               |
| current   | Display the current folder                                | current                                      |
| goto      | Set the current folder                                    | goto C:\Projects                       |
| dirs      | Display the available folders                             | dirs                                         |
| large     | Show the largest files in the folder                      | large                                        |
| setsize   | Set the threshold size for identifying large files (in MB)| setsize 500                                  |
| show      | Display the contents of the current folder                | show OR show D:\Torrents                    |
| cd        | Change the current working directory to the specified path| cd venv                                     |
| ..        | Move up one level in the directory tree                   | ..                                           |
| stats     | Show statistics about file types and sizes                | stats                                        |
| permissions| Show files with unusual permissions (World-writable or Read-only)| permissions                          |


![Example](https://github.com/Thoughtseize1/File_System_Insight_Tool/blob/main/example/Example.png)
