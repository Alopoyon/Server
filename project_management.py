import pathlib
from pathlib import Path
import pdfplumber as pdf

class ProjectManagement:
    def __init__(self,directory: pathlib.WindowsPath):
        self._directory_contents = directory

    def _return_directory_names(self):
        __project_directories = []
        # print(f"{self._directory_contents=}")
        for directory in self._directory_contents.iterdir():
            # print(f"{directory=}")
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
        if self._directory_contents.is_file():
            print("File check passed")
            _dat = self.read_file_contents()
            return _dat

        _directory_contents = {
            "directories": self._return_directory_names(),
            "files": self._return_file_names()
        }
        return _directory_contents
    
    def read_file_contents(self):
        _extension = self._directory_contents.suffix
        print("EXT: ",_extension)
        _dat = ""
        if _extension == ".pdf":
            with pdf.open(self._directory_contents) as pdf_file:
                for page in pdf_file.pages:
                    _dat += page.extract_text()
        if _extension == ".txt":
            with open(self._directory_contents,'rb') as f:
                _dat = f.read()
        print("DAT: ",_dat)
        return _dat
        
    def __str__(self):
        if self._directory_contents.exists():
            return str(self._directory_contents.resolve())
        return "Invalid"