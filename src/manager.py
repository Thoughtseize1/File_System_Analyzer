import os

from tabulate import tabulate
import stat


class Config():
    colors = {
        "RESET": "\033[0m",
        "YELLOW": "\033[33m",
        "CYAN": "\033[36m",
        "RED": "\033[31m"
    }
    unusual_permissions = {
        "World-writable": "-rwxrwxrwx",  # 777
        "Read-only": "-r--r--r--"  # 555
    }
    DEFAULT_MAX_FILE_SIZE_MB = 500
    ONE_KILOBYTE = 1024
    TABLE_FORMATS = ["plain", "simple", "github", "grid", "fancy_grid"]

    def __init__(self, max_file_size=None):
        if max_file_size is None:
            max_file_size = self.DEFAULT_MAX_FILE_SIZE_MB
        self.skipped_dir_names = ["venv", ".git", "__pycache__", ".idea", "build"]
        self._max_file_size = self._convert_mb_to_bytes(max_file_size)
        self._selected_format = self.TABLE_FORMATS[4]
        self._str_max_file_size_in_mb = self.convert_size_to_str(self._max_file_size)

    def _convert_mb_to_bytes(self, size_in_mb):
        """
        The _convert_mb_to_bytes function converts a size in megabytes to bytes.

        :param self: Represent the instance of the class
        :param size_in_mb: Convert the size of a file from megabytes to bytes
        :return: The size in bytes
        """
        return size_in_mb * self.ONE_KILOBYTE * self.ONE_KILOBYTE

    def convert_size_to_str(self, size_in_bytes):
        """
        The convert_size_to_str function takes a size in bytes and converts it to a human-readable string.

        :param self: Reference the object itself
        :param size_in_bytes: Convert the size of a file into bytes
        :return: A string that represents the size of a file in bytes, kilobytes, megabytes or gigabytes
        """
        size_in_kb = size_in_bytes / self.ONE_KILOBYTE
        if size_in_kb < 1:
            return f"{size_in_bytes} bytes"
        elif size_in_kb < self.ONE_KILOBYTE:
            return f"{size_in_kb:.2f} KB"
        elif size_in_kb < self.ONE_KILOBYTE * self.ONE_KILOBYTE:
            size_in_mb = size_in_kb / self.ONE_KILOBYTE
            return f"{size_in_mb:.2f} MB"
        else:
            size_in_gb = size_in_kb / (self.ONE_KILOBYTE * self.ONE_KILOBYTE)
            return f"{size_in_gb:.2f} GB"


class FolderManager(Config):
    TEXT_EXTENSIONS = ['.txt', '.csv', '.docx', '.pdf']
    IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', 'HEIC']
    EXECUTABLE_EXTENSIONS = ['.exe', '.dll', '.bat']
    VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv', '.mov', '.ts']

    def __init__(self):
        super().__init__()
        self.current_folder = os.getcwd()
        self.folder = {}
        self.file_categories = {}
        self.large_files = {}
        self.initialize_categories()
        self.unusual_perm_files = []

    def initialize_categories(self):
        """
        The initialize_categories function initializes the file_categories dictionary with keys for each category of files.
        Each key is associated with a dictionary containing the extensions that belong to that category, an empty list of files, and a size value initialized to 0.

        :return: A dictionary with the following keys:
        """
        self.file_categories = {
            'Text Files': {"extensions": self.TEXT_EXTENSIONS, "files": [], "category_size": 0},
            'Image Files': {"extensions": self.IMAGE_EXTENSIONS, "files": [], "category_size": 0},
            'Video Files': {"extensions": self.VIDEO_EXTENSIONS, "files": [], "category_size": 0},
            'Executable Files': {"extensions": self.EXECUTABLE_EXTENSIONS, "files": [], "category_size": 0},
            'Other Files': {"extensions": [], "files": [], "category_size": 0},
        }

    def analyse_folder(self, *args):
        """
        Analyze the specified folder by collecting information about its subfolders and files.

        This function collects data about the specified folder using the `collect_folder` method.
        If the folder is successfully collected and processed, it prints a message indicating that the analysis is complete.

        :param args: Optional folder path to be analyzed. Arguments provided by the user, representing the path to the folder (if provided).
                    If no arguments are provided, it analyzes the current folder self.current_folder.
        :return: None
        """
        if self.collect_folder(*args):
            print(f"Folder {self.current_folder} has been analyzed!")

    def categorize_file(self, file_path, file_size):
        """
        The categorize_file function takes a file path and size as arguments.
        It then determines the category of the file based on its extension,
        and adds it to that category's list of files. It also updates the total size for that category.

        :param file_path: Get the file extension and to get the permissions of a file
        :param file_size: Get the size of a file.
        :return: None
        """
        file_extension = os.path.splitext(file_path)[-1].lower()
        category = self.get_category(file_extension)
        category['files'].append((file_path, file_size))
        category['category_size'] += file_size

        # PERMISSIONS
        permissions = os.stat(file_path).st_mode
        permissions = stat.filemode(permissions)
        # Добавление файлов с необычными разрешениями в список
        if permissions in self.unusual_permissions.values():
            self.unusual_perm_files.append((file_path, permissions))

    def get_category(self, file_extension):
        """
        Determine the category of a file based on its extension.

        It iterates through predefined file categories and their associated extensions to determine the appropriate category.
        If the file extension does not match any predefined category, it falls back to the 'Other Files' category.

        :param file_extension: The file extension to determine the category.
        :return: Dictionary representing the file category with its extensions, files, and category size.
        """
        for category, info in self.file_categories.items():
            if file_extension in info["extensions"]:
                return info
        return self.file_categories['Other Files']

    def collect_folder(self, *args):
        """
        Collect information about the specified folder by processing its subfolders and files.

        This function resets the existing data, sets the current folder based on the provided arguments, and then
        processes the subfolders and files within the specified folder. If the folder does not exist or an error occurs,
        appropriate messages are printed.

        :param *args: Optional folder path to be analyzed.Arguments provided by the user, representing the path to the folder (if provided).
        If no arguments are provided, it analyzes the current folder in self.current_folder.
        :return: True if the folder is successfully collected and processed, False otherwise.
        """
        self.reset_data()
        self.set_current_folder(args)
        if not os.path.exists(self.current_folder) or not os.path.isdir(self.current_folder):
            print("The folder does not exist.")
            return False
        try:
            self.process_folders_and_files()
            return True
        except FileNotFoundError:
            print(f"Folder {self.current_folder} not found.")
        except Exception as e:
            print(f"ERROR: {e}")
        return False

    def process_folders_and_files(self):
        """
        Process subfolders and files within the specified folder.

        This function calculates the total size of the folder and iterates through its subfolders and files,
        processing each subfolder using 'process_subfolders()' and each file using 'process_files()'.

        :return: None
        """
        self.folder["total_folder_size"] = 0
        for root, dirs, files in os.walk(self.current_folder):
            self.process_subfolders(root, dirs)
            self.process_files(root, files)

    def process_subfolders(self, root, dirs):
        """
        Process subfolders within the specified root folder.

        This function filters out skipped directory names, updates the 'self.folder' dictionary with subfolder information.

        :param root: The root folder path.
        :param dirs: List of subfolders in the root folder.
        :return: None
        """
        dirs[:] = [dir for dir in dirs if dir not in self.skipped_dir_names]
        self.folder[root] = ""

    def process_files(self, root, files):
        """
        Process files within the specified root folder.

        This function iterates over the list of files, calculates file size, updates the total folder size,
        categorizes the file, and updates the 'self.folder' dictionary with file information.

        :param root: The root folder path.
        :param files: List of files in the root folder.
        :return: None
        """
        for file in files:
            file_path = None
            try:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                self.folder["total_folder_size"] += file_size
                if file_size >= self._max_file_size:
                    self.large_files[file_path] = self.convert_size_to_str(file_size)
                self.categorize_file(file_path, file_size)
                self.folder[root] += f"{file} - {self.convert_size_to_str(file_size)}\n"
            except OSError as e:
                print(f"Error accessing {file_path}: {e}")

    def reset_data(self):
        """
        Reset data attributes, clearing existing folder, categories, large files, and unusual permission files.

        :return: None
        """
        self.folder = {}
        self.initialize_categories()
        self.large_files = {}
        self.unusual_perm_files = []

    def set_max_size(self, *args):
        """
        Set the maximum size for files in megabytes.

        :param *args: Arguments provided by the user, representing the maximum file size in megabytes.
        :return: None
        """
        try:
            self._max_file_size = self._convert_mb_to_bytes(int(args[0]))
            self._str_max_file_size_in_mb = self.convert_size_to_str(self._max_file_size)
            self.collect_folder()
            print(f'Max size for file setted to {self._str_max_file_size_in_mb}')
        except (IndexError, ValueError):
            print(
                f"Invalid size. You should write size in MB.\n{self.colors['YELLOW']}Example:{self.colors['RESET']} setsize 450")

    def set_current_folder(self, args):
        """
        Set the current working folder based on the provided arguments.

        If arguments are provided, it sets the current folder to the joined path of the provided arguments.
        If no arguments are provided and the current folder is the same as the current working directory,
        it prints a message indicating the current folder.

        :param args: Optional folder path provided by the user.
                     If provided, it sets the current folder to the joined path of the arguments.
        """
        if args:
            self.current_folder = " ".join(args)
        elif self.current_folder == os.getcwd():
            print(f"You are in {self.current_folder}")

    def show_current_folder(self, *args):
        """
        Display the current folder path.

        :param *args: Additional arguments (not used in this function).
        :return: None
        """
        print(f"Current folder is {self.current_folder}")

    def display_folder_data(self, *args):
        """
        Display information about the content of the folder in a table format using tabulate.

        This function collects and processes the folder data, then prints the folder and files information in a tabular format.
        If folder size information is available, it is also displayed.

        :param *args: Optional folder path to be analyzed. Arguments provided by the user, representing the path to the folder (if provided).
                      If no arguments are provided, it analyzes the current folder.
        :return: None
        """
        if self.collect_folder(*args):
            table_data = []
            folder_size = self.folder.pop('total_folder_size', None)
            for folder, files_info in self.folder.items():
                table_data.append([folder, files_info])
            table = tabulate(table_data, headers=["Folder", "Files"], tablefmt=self._selected_format)
            print(table)
            if folder_size:
                print(f"Total folder size: {self.convert_size_to_str(folder_size)}")

    def display_largest_files(self):
        """
        Display a table with files larger than the specified size limit.

        If there are large files, it prints a table with file paths and sizes. If no large files are found,
        it prints a message indicating that the list is empty, and the current size limit is displayed.

        :return: None
        """
        if self.large_files:
            print(
                f"{self.colors['CYAN']}TABLE WITH FILES MORE THAT {self.convert_size_to_str(self._max_file_size)}{self.colors['RESET']}")
            table_data = []

            # Проходимся по словарю и добавляем данные в формате [Путь к файлу, Размер файла]
            for file_path, file_size in self.large_files.items():
                table_data.append([file_path, file_size])
            table = tabulate(table_data, headers=["File", "Size"], tablefmt=self._selected_format)
            print(table)
        else:
            print(
                f"List of large files is emply. You should analyze the folder first.\nCurrent size limit = {self._str_max_file_size_in_mb}")

    def display_permissions(self):
        """
        Display files with unusual permissions.

        If there are files with unusual permissions, it prints a table containing file paths and corresponding permissions.
        If no such files are found, it prints a message indicating that there are no unusual permissions in files.

        :return: None
        """
        if self.unusual_perm_files:
            print(
                f"{self.colors['RED']}Unusual permissions:{self.colors['RESET']}")
            table = tabulate(self.unusual_perm_files, headers=["File", "Permission"], tablefmt=self._selected_format)
            print(table)
        else:
            print("There are no unusual permissions in files")

    def display_size_by_extension(self):
        """
        Display a table showing the sizes of different file categories based on their extensions.

        If the folder has been analyzed, it prints a table with file categories and their respective sizes.
        If the folder has not been analyzed, it prompts the user to run the analysis first.

        :return: None
        """
        if self.folder.get("total_folder_size"):
            table_data = []
            for category, category_info in self.file_categories.items():
                table_data.append([category, self.convert_size_to_str(category_info['category_size'])])
            table = tabulate(table_data, headers=["Files type", "Category size"], tablefmt="grid")
            print(table)
        else:
            print("The folder has not been analyzed yet. Please run the analysis first.")


manager = FolderManager()
