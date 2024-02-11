import os
import unittest
from unittest.mock import patch, mock_open, MagicMock
from src.manager import FolderManager


class TestFolderManager(unittest.TestCase):

    def setUp(self):
        # Мокаем функцию os.path.exists для возврата True вместо реальной проверки
        self.exists_patch = patch('os.path.exists', MagicMock(return_value=True))
        self.exists_patch.start()

        # Мокаем функцию os.path.isdir для возврата True вместо реальной проверки
        self.isdir_patch = patch('os.path.isdir', MagicMock(return_value=True))
        self.isdir_patch.start()

        # Мокаем функцию os.walk для возврата фиктивных данных
        self.walk_patch = patch('os.walk', MagicMock(return_value=('/test_folder', [], ['large_file.txt'])))
        self.walk_patch.start()

    def tearDown(self):
        self.exists_patch.stop()
        self.isdir_patch.stop()
        self.walk_patch.stop()

    @patch('os.path.exists', return_value=True)
    @patch('os.path.isdir', return_value=True)
    @patch('os.walk', return_value=[('/test_folder', ['subfolder'], ['file.txt'])])
    def test_collect_folder_success(self, mock_walk, mock_isdir, mock_exists):
        manager = FolderManager()
        result = manager.collect_folder('/test_folder')
        self.assertTrue(result)

    @patch('os.path.exists', return_value=False)
    def test_collect_folder_folder_not_exist(self, mock_exists):
        manager = FolderManager()
        result = manager.collect_folder('/nonexistent_folder')
        self.assertFalse(result)

    @patch('os.path.exists', return_value=True)
    @patch('os.path.isdir', return_value=True)
    @patch('os.walk', return_value=[('\\test_folder', ['subfolder'], ['large_file.txt'])])
    def test_process_files_large_file(self, mock_walk, mock_isdir, mock_exists):
        manager = FolderManager()
        manager._max_file_size = 1024  # Small size just for example

        with patch('builtins.open', mock_open(read_data='mocked file content')):
            with patch('os.path.getsize', return_value=2048):
                manager.collect_folder('/test_folder')

        # Нормализуем путь и заменяем обратные слеши на прямые
        normalized_path = os.path.normpath(os.path.join('/test_folder', 'large_file.txt'))
        virtual_path = f'{normalized_path}'

        self.assertEqual(virtual_path, next(iter(manager.large_files.keys())))
        self.assertEqual(manager.large_files[virtual_path], '2.00 KB')

    def test_reset_data(self):
        manager = FolderManager()
        manager.folder = {'test_folder': 'test_file.txt', 'Passwords': 'my_passwords_from_all_websites.txt'}
        manager.large_files = {'large_file.txt': '2 MB'}
        manager.unusual_perm_files = [('unusual_file.txt', 'rwxrwxrwx')]
        manager.reset_data()
        self.assertEqual(manager.folder, {})
        self.assertEqual(manager.large_files, {})
        self.assertEqual(manager.unusual_perm_files, [])

    @patch('os.path.exists', return_value=True)
    @patch('os.path.isdir', return_value=True)
    @patch('os.walk', return_value=[('/test_folder', ['subfolder'], ['large_file.txt'])])
    def test_set_max_size_valid_input(self, mock_walk, mock_isdir, mock_exists):
        manager = FolderManager()

        # Вызываем функцию set_max_size с валидным вводом
        with patch.object(manager, 'collect_folder') as mock_collect_folder:
            manager.set_max_size('500')

            # Проверяем, что атрибуты установлены правильно
            self.assertEqual(manager._max_file_size, 500 * manager.ONE_KILOBYTE * manager.ONE_KILOBYTE)
            self.assertEqual(manager._str_max_file_size_in_mb, '500.00 MB')


if __name__ == '__main__':
    unittest.main()
