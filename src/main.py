from src.parser import parser
from src.manager import manager


def main():
    """ Main function - all interaction with user """
    print(
        f"{manager.colors['YELLOW']}HELLO MAN! How can i help you? Use can type 'help' to get available commands{manager.colors['RESET']}")
    try:
        while True:
            msg = input(f"{manager.colors['CYAN']}Input command{manager.colors['RESET']}: ")
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
