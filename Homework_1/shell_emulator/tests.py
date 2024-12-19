import unittest
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        config = {
            'filesystem_path': 'shell_emulator.zip',
            'log_file_path': 'log.xml'
        }
        self.emulator = ShellEmulator(config)

    def test_ls(self):
        self.emulator.ls()
        # Проверьте вывод или состояние после выполнения команды ls

    def test_cd(self):
        self.emulator.cd('test_directory')
        self.assertEqual(self.emulator.current_directory, 'test_directory')

    def test_clear(self):
        # Необходимо проверить, что экран очищается
        self.emulator.clear()
        # Проверка может быть сложной, но можно использовать mock для проверки вызова os.system

    def test_head(self):
        self.emulator.head('test_file.txt')
        # Проверьте вывод или состояние после выполнения команды head

if __name__ == '__main__':
    unittest.main()
