from src.functions import hello_func, goodbye, directory_traversal, show_folder_content, show_folder_content2

OPERATIONS = {
    'hello': hello_func,
    "bye": goodbye,
    'exit': goodbye,
    'showdirs': directory_traversal,
    'show': show_folder_content,
    'sh': show_folder_content2
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
