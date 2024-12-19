import os
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime

class ShellEmulator:
    def __init__(self, config):
        self.filesystem_path = config['filesystem_path']
        self.log_file_path = config['log_file_path']
        self.current_directory = '/'
        self.log = []

    def log_action(self, action):
        timestamp = datetime.now().isoformat()
        self.log.append(f"<action><timestamp>{timestamp}</timestamp><command>{action}</command></action>")

    def save_log(self):
        root = ET.Element("log")
        for entry in self.log:
            root.append(ET.fromstring(entry))
        tree = ET.ElementTree(root)
        tree.write(self.log_file_path)

    def ls(self):
        with zipfile.ZipFile(self.filesystem_path, 'r') as z:
            file_list = z.namelist()
            for file in file_list:
                print(file)
        self.log_action("ls")

    def cd(self, directory):
        # В данном случае просто имитируем переход в каталог
        self.current_directory = directory
        self.log_action(f"cd {directory}")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.log_action("clear")

    def head(self, filename):
        with zipfile.ZipFile(self.filesystem_path, 'r') as z:
            with z.open(filename) as f:
                print(f.read(100))  # Читаем первые 100 байт
        self.log_action(f"head {filename}")

    def exit(self):
        self.save_log()
        print("Exiting shell emulator.")
        self.log_action("exit")
        exit(0)

    def run(self):
        while True:
            command = input(f"{self.current_directory} $ ")
            parts = command.split()
            cmd = parts[0]

            if cmd == 'ls':
                self.ls()
            elif cmd == 'cd':
                if len(parts) > 1:
                    self.cd(parts[1])
                else:
                    print("cd: missing argument")
            elif cmd == 'clear':
                self.clear()
            elif cmd == 'head':
                if len(parts) > 1:
                    self.head(parts[1])
                else:
                    print("head: missing argument")
            elif cmd == 'exit':
                self.exit()
            else:
                print(f"{cmd}: command not found")
if __name__ == "__main__":
    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')
    emulator = ShellEmulator(config['settings'])
    emulator.run()
