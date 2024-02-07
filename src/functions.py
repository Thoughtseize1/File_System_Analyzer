import os

from faker import Faker
from tabulate import tabulate


class Config():

    def __init__(self, max_file_size=1024):
        self._size_threshold = max_file_size
        self.skipped_dir_names = ["venv", ".git", "__pycache__", ".idea"]

    def set_size(self, new_max_size):
        self._size_threshold = new_max_size


class Viewer():
    def __init__(self, max_file_size=1024):
        self.list_of_dirs = []
        self.list_of_files = []


fake = Faker()
config = Config()


def hello_func(*args):
    print(fake.name())


def goodbye(*args):
    """Function to end program"""
    print("Goodbye!")
    quit()


columns = ['Folder', 'Files']


def directory_traversal(*args):
    if not args:
        args = os.path.dirname(os.path.abspath(__file__))

    for root, dirs, files in os.walk(args[0]):
        table = []
        # print(f"Folder: {root}")
        dirs[:] = [dir for dir in dirs if dir not in config.skipped_dir_names]
        print(dirs)
        print(files)
        files_list = [file for file in files]
        table.append([root, files_list])
        # for file in files:
        #     print(f"  File: {file}")
        for dir_ in dirs:
            directory_traversal(os.path.join(root, dir_))
        # if table:
        #     print(tabulate(table, headers=["Folder", "Files"], tablefmt="psql"))


def show_folder_content(folder_path):
    """
    Функция для отображения содержимого папки и её подпапок в виде таблицы.
    """
    try:
        # Получаем список файлов и подпапок в указанной папке
        content_list = os.listdir(folder_path)

        # Сортируем список файлов и папок
        content_list = sorted(content_list)

        # Создаем список для хранения данных таблицы
        table_data = []

        # Добавляем корневую папку в таблицу
        table_data.append([folder_path, ""])

        # Проходимся по каждому элементу в списке
        for content_item in content_list:
            # Формируем полный путь к элементу
            content_item_path = os.path.join(folder_path, content_item)

            # Проверяем, является ли элемент папкой
            if os.path.isdir(content_item_path):
                # Если это папка, рекурсивно вызываем функцию для отображения её содержимого
                show_folder_content(content_item_path)
            else:
                # Если это файл, добавляем его в список файлов текущей папки
                table_data[-1][1] += f"{content_item}\n"

        # Выводим таблицу
        print(tabulate(table_data, headers=["Папка", "Файлы"], tablefmt="grid"))

    except FileNotFoundError:
        print(f"Папка {folder_path} не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def show_folder_content2(folder_path):
    """
    Функция для отображения содержимого папки и её подпапок в виде таблицы, используя os.walk().
    """
    try:
        # Создаем список для хранения данных таблицы
        table_data = []
        # Проходимся по всем папкам и подпапкам в указанной директории
        for root, dirs, files in os.walk(folder_path):
            # Добавляем текущую папку в таблицу
            table_data.append([root, ""])
            # Проходимся по каждому файлу в текущей папке
            for file in files:
                # Добавляем файл в список файлов текущей папки
                table_data[-1][1] += f"{file}\n"
        # Выводим таблицу
        print(tabulate(table_data, headers=["Folder", "Files"], tablefmt="grid"))
    except FileNotFoundError:
        print(f"Folder {folder_path} not found.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")





# def file_ype_ategorization(*args):
#     # TODO document why this method is empty WD
#     pass
#
#
# def size_analysis(*args):
#     # TODO document why this method is empty
#     pass
#
#
# def large_files_identification(*args):
#     # TODO document why this method is empty
#     pass
