from tabulate import tabulate
def hello_func(*args):
    print("Hello dear user! Welcome to the File System Insight Tool.")
    print("You can use the command 'help' to see available commands and their descriptions.")



def goodbye(*args):
    """Function to end program"""
    print("Goodbye!")
    quit()


def display_command_help(*args):
    commands_info = [
        ["hello/hi", "Display a greeting message", "hello"],
        ["bye/exit", "End the program", "bye"],
        ["help", "Display command help", "help"],
        ["current", "Display the current folder", "current"],
        ["goto", "Set the current working folder based on the provided arguments.", "goto C:\\YourFolder"],
        ["dirs", "Display the current folder path and available subfolders.", "dirs"],
        ["cd", "Change the current working directory to the specified path.", "cd venv"],
        ["..", "Move one level up in the directory hierarchy.", ".."],
        ["analyze", "Analyze the specified folder", "analyze OR analyze D:\Torrents"],
        ["show", "Display the contents of the current folder", "show OR show D:\Torrents"],
        ["large", "Show the largest files in the folder", "largest"],
        ["setsize", "Set the threshold size for identifying large files (in MB)", "setsize 500"],
        ["stats", "Show statistics about file types and sizes", "stats"],
        ["permissions", "Show files with unusual permissions\nWorld-writable or Read-only", "permissions"]
    ]

    headers = ["Command", "Description", "Example"]
    table = tabulate(commands_info, headers, tablefmt="grid")
    print(table)