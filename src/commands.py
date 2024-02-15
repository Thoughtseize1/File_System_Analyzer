from tabulate import tabulate

from src.manager import manager


def display_command_help(*args):
    table_data = [(key, value["description"], value["example"]) for key, value in OPERATIONS.items()]
    headers = ["Command", "Description", "Example"]
    table = tabulate(table_data, headers, tablefmt="grid")
    print(table)


def goodbye(*args):
    """Function to end program"""
    print("Goodbye!")
    quit()


OPERATIONS = {
    'help': {
        "cmd": display_command_help,
        "description": "Display command help",
        "example": "help"
    },
    'bye': {
        "cmd": goodbye,
        "description": "Say goodbye",
        "example": "bye"
    },
    'exit': {
        "cmd": goodbye,
        "description": "Exit the program",
        "example": "exit"
    },
    'analyze': {
        "cmd": manager.analyse_folder,
        "description": "Analyze the contents of a folder. The current folder will be analyzed if command will be called without parameters",
        "example": "analyze OR analyze D:\Torrents"
    },
    'goto': {
        "cmd": manager.set_current_folder,
        "description": "Set the current working folder based on the provided arguments.",
        "example": "goto <folder_path>"
    },
    'dirs': {
        "cmd": manager.show_dirs,
        "description": "Display the current folder path and available subfolders.",
        "example": "dirs"
    },
    'large': {
        "cmd": manager.display_largest_files,
        "description": "Display the largest files in the current folder",
        "example": "large"
    },
    'setsize': {
        "cmd": manager.set_max_size,
        "description": "Set the threshold size for identifying large files (in MB)",
        "example": "setsize <size>"
    },
    'show': {
        "cmd": manager.display_folder_data,
        "description": "Display the contents of the current folder",
        "example": "show OR show <folder_path>"
    },
    "cd": {
        "cmd": manager.join_dir,
        "description": "Change the current working directory to the specified path.",
        "example": "cd <directory> OR cd venv"
    },
    "..": {
        "cmd": manager.go_up_one_level,
        "description": "Move up one level in the directory structure",
        "example": ".."
    },
    'stats': {
        "cmd": manager.display_size_by_extension,
        "description": "Show statistics about file types and sizes",
        "example": "stats"
    },
    'permissions': {
        "cmd": manager.display_permissions,
        "description": "Show files with unusual permissions\nWorld-writable or Read-only",
        "example": "permissions"
    },
    'ignore': {
        "cmd": manager.display_ignoring_folders,
        "description": "Display the list of folders currently marked to be ignored during analysis. Ignored folders will be excluded from the analysis process.",
        "example": "ignore"
    },
    'addignore': {
        "cmd": manager.add_to_ignore_list,
        "description": "Add a folder to the list of ignored folders. Folders in this list will not be analyzed in subsequent operations.",
        "example": "addignore"
    }
}
