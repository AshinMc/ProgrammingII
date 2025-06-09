import os

def color_decorator(color: str):
    """Decorator that changes text color using ANSI codes."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "end": "\033[0m"
    }
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors.get(color, colors['end'])}{result}{colors['end']}"
        return wrapper
    return decorator

class FileReader:
    """Class for reading and manipulating text files."""
    
    def __init__(self, file_path):
        """Initialize with a file path."""
        self._file_path = file_path
    
    @property
    def file_path(self):
        """Getter for file path."""
        return self._file_path
    
    @file_path.setter
    def file_path(self, value):
        """Setter for file path."""
        self._file_path = value
    
    def read_lines(self):
        """Generator that yields lines from the file."""
        if not os.path.exists(self._file_path):
            yield f"File not found: {self._file_path}"
            return
            
        with open(self._file_path, 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    
    @staticmethod
    def file_exists(path):
        """Check if a file exists."""
        return os.path.exists(path)
    
    @classmethod
    def from_directory(cls, directory, filename):
        """Create FileReader from directory and filename."""
        return cls(os.path.join(directory, filename))
    
    def __str__(self):
        """String representation of FileReader."""
        return f"FileReader({self._file_path})"
    
    def __add__(self, other):
        """Concatenate contents of two files using + operator."""
        if not isinstance(other, FileReader):
            raise ValueError("Can only add FileReader instances")
        
        content = ""
        if not os.path.exists(self._file_path):
            content += f"[File not found: {self._file_path}]\n"
        else:
            with open(self._file_path, 'r') as f1:
                content += f1.read()
                
        if not os.path.exists(other._file_path):
            content += f"[File not found: {other._file_path}]\n"
        else:
            with open(other._file_path, 'r') as f2:
                content += f2.read()
                
        return content
    
    def concat_files(self, *file_paths):
        """Concatenate contents of any number of files."""
        content = ""
        for path in (self._file_path,) + file_paths:
            if not os.path.exists(path):
                content += f"[File not found: {path}]\n"
            else:
                with open(path, 'r') as f:
                    content += f.read()
        return content

class ColoredFileReader(FileReader):
    """Enhanced FileReader with colored output capabilities."""
    
    @color_decorator("red")
    def __str__(self):
        """Colored string representation."""
        return super().__str__()
    
    @color_decorator("green")
    def concat_files(self, *file_paths):
        """Override to add colored formatting to concatenated content."""
        result = super().concat_files(*file_paths)
        return f"--- Concatenated Content ---\n{result}"
    
    @color_decorator("blue")
    def read_lines(self):
        """Return colored list of lines from file."""
        return [line for line in super().read_lines()]

# Example usage
if __name__ == "__main__":
    # Basic FileReader usage
    fr1 = FileReader("file1.txt")
    fr2 = FileReader("file2.txt")
    print(fr1)
    print(fr1 + fr2)  # Using __add__
    
    # ColoredFileReader usage
    cfr = ColoredFileReader("file1.txt")
    print(cfr)  # Colored output
    print(cfr.concat_files("file2.txt", "file3.txt"))