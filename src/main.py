from src.parser import parser

RESET_COLOR = "\033[0m"
YELLOW_COLOR = "\033[33m"
CYAN_COLOR = "\033[36m"
RED_COLOR = "\033[31m"


def main():
    """ Main function - all interaction with user """
    print(f"{YELLOW_COLOR}HELLO MAN! How can i help you? Use can type 'help' to get available commands{RESET_COLOR}")
    while True:
        meow = 0
        msg = input(f"{CYAN_COLOR}Input command{RESET_COLOR}: ")
        command, params = parser(msg)
        if command:
            command(*params)
            meow += 1
            if meow == 4:
                print('Meow!')
                meow = 0
        else:
            print(f"{RED_COLOR}No command specified")


if __name__ == '__main__':
    main()
