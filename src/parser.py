import src.functions as funcs
from src.manager import manager

OPERATIONS = {
    'help': funcs.display_command_help,
    'hello': funcs.hello_func,
    'hi': funcs.hello_func,
    'bye': funcs.goodbye,
    'exit': funcs.goodbye,
    'analyze': manager.analyse_folder,
    'current': manager.show_current_folder,
    'goto': manager.set_current_folder,
    'dirs': manager.show_dirs,
    'large': manager.display_largest_files,
    'setsize': manager.set_max_size,
    'show': manager.display_folder_data,
    "cd": manager.join_dir,
    "..": manager.go_up_one_level,
    'stats': manager.display_size_by_extension,
    'permissions': manager.display_permissions
}


def parser(msg: str):
    """ Parser and handler AIO """
    command = None
    params = []

    for key in OPERATIONS:
        if msg.lower().startswith(key):
            command = OPERATIONS[key]
            msg = msg.lstrip(key)
            for item in filter(lambda x: x != '', msg.split(' ')):
                params.append(item)
            return command, params
    return command, params
