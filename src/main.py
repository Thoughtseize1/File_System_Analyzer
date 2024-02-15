from src.manager import manager
from src.commands import OPERATIONS


def parser(msg: str):
    """ Parser and handler AIO """
    command = None
    params = []

    for key in OPERATIONS:
        if msg.lower().startswith(key):
            command = OPERATIONS[key]["cmd"]
            msg = msg.lstrip(key)
            for item in filter(lambda x: x != '', msg.split(' ')):
                params.append(item)
            return command, params
    return command, params


def main():
    """ Main function - all interaction with user """
    print(
        f"{manager.colors['YELLOW']}Hello dear user!\nWelcome to the File System Insight Tool.\nHow can I help you? Use can type 'help' to see available commands{manager.colors['RESET']}")
    try:
        while True:
            msg = input(
                f"{manager.colors['CYAN']}Input your command\n{manager.colors['YELLOW']}{manager.current_folder}{manager.colors['RESET']}:")
            command, params = parser(msg)
            if command:
                command(*params)
            else:
                print(f"{manager.colors['RED']}No command specified. Use the command 'help' to see available commands")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()


if __name__ == '__main__':
    main()
