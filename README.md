

# File System Insight Tool
A command-line tool that analyzes and reports on the file system structure and usage on a Linux system.


## Description

File System Insight Tool is a tool for analyzing the file system. It provides detailed information about the content of a specified folder, categorizing files by types and sizes.

## Features

 - Analysis of folder content and its subfolders.
 - Categorization of files by types (text files, images, video files, etc.) based on their extensions.
 - Calculates and displays the total size for each file type category.
 - Detection of large files with the ability to set a custom size threshold.
 - Generation a report of files that have permission settings that are unusual (for instance, world-writable files).   
 - Robust error handling for scenarios like inaccessible directories.

## Requirements

- Python 3.x
- Access to the file system for analyzing folders

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Thoughtseize1/File_System_Insight_Tool
    cd file-system-insight-tool
## Avaliable commands

| Command      | Description                                 | Example                                  |
|--------------|---------------------------------------------|------------------------------------------|
| `hello`      | Display a greeting message                  | `hello`                                  |
| `bye/exit`   | End the program                             | `bye`                                    |
| `analyze`    | Analyze the specified folder                | `analyze OR analyze D:\Torrents`        |
| `show`       | Display the contents of the current folder  | `show OR show D:\Torrents`               |
| `large`      | Show the largest files in the folder        | `largest`                                |
| `setsize`    | Set the threshold size for identifying large files (in MB) | `setsize 500`                    |
| `current`    | Display the current folder                  | `current`                               |
| `stats`      | Show statistics about file types and sizes  | `stats`                                 |
| `permissions`| Show files with unusual permissions<br>World-writable or Read-only | `permissions`            |

![Example](https://i.im.ge/2024/02/11/cASVaS.Screenshot-2024-02-11-171202.png)
