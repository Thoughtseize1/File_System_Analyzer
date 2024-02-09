from tabulate import tabulate
def hello_func(*args):
    print("Hello dear user!")


def goodbye(*args):
    """Function to end program"""
    print("Goodbye!")
    quit()


def display_command_help(*args):
    commands_info = [
        ["hello", "Display a greeting message", "hello"],
        ["bye/exit", "End the program", "bye"],
        ["analyze", "Analyze the specified folder", "analyze OR analyze D:\Torrents"],
        ["show", "Display the contents of the current folder", "show OR show D:\Torrents"],
        ["large", "Show the largest files in the folder", "largest"],
        ["setsize", "Set the threshold size for identifying large files (in MB)", "setsize 500"],
        ["current", "Display the current folder", "current"],
        ["stats", "Show statistics about file types and sizes", "stats"],
        ["permissions", "Show files with unusual permissions\nWorld-writable or Read-only", "permissions"]
    ]

    headers = ["Command", "Description", "Example"]
    table = tabulate(commands_info, headers, tablefmt="grid")
    print(table)