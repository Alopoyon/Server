import pathlib
from pathlib import Path

class ProjectManagement:
    def __init__(self,directory: pathlib.WindowsPath):
        self._directory_contents = directory

    def _return_directory_names(self):
        __project_directories = []
        for directory in self._directory_contents.iterdir():
            if directory.is_dir():
                __project_directories.append(directory.name)

        return __project_directories

    def _return_file_names(self):
        __project_files = []
        for file in self._directory_contents.iterdir():
            if file.is_file():
                __project_files.append(file.name)

        return __project_files

    def directory_contents(self):
        _directory_contents = {
            "directories": self._return_directory_names(),
            "files": self._return_file_names()
        }
        return _directory_contents
    
    def read_file_contents(self):
        with self._directory_contents.open() as f:
            _dat = f.read()
        return _dat