"""Reading and manipulating text files with color output."""

import os

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "end": "\033[0m",
}


def color_decorator(color: str):
    """Apply ANSI color formatting to function output."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors.get(color, colors['end'])}{result}{colors['end']}"

        return wrapper

    return decorator


class FileReader:
    """Read and manipulate text files."""

    def __init__(self, file_path):
        """Initialize with file path."""
        self._file_path = file_path

    @property
    def file_path(self):
        """Get file path."""
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        """Set file path."""
        self._file_path = value

    def read_lines(self):
        """Generate lines from file one at a time."""
        if not os.path.exists(self._file_path):
            yield f"File not found: {self._file_path}"
            return

        with open(self._file_path, "r") as f:
            for line in f:
                yield line.rstrip("\n")

    @staticmethod
    def file_exists(path):
        """Check if file exists."""
        return os.path.exists(path)

    @classmethod
    def from_directory(cls, directory, filename):
        """Create FileReader from directory and filename."""
        return cls(os.path.join(directory, filename))

    def __str__(self):
        """Return file contents as string."""
        if not os.path.exists(self._file_path):
            return f"File not found: {self._file_path}"

        with open(self._file_path, "r") as f:
            return f.read()

    def __add__(self, other):
        """Concatenate contents of two files."""
        if not isinstance(other, FileReader):
            raise ValueError("Can only add FileReader instances")

        content = ""
        if not os.path.exists(self._file_path):
            content += f"[File not found: {self._file_path}]\n"
        else:
            with open(self._file_path, "r") as f1:
                content += f1.read()

        if not os.path.exists(other._file_path):
            content += f"[File not found: {other._file_path}]\n"
        else:
            with open(other._file_path, "r") as f2:
                content += f2.read()

        return content

    def concat_files(self, *file_paths):
        """Concatenate contents of multiple files."""
        content = ""
        for path in (self._file_path,) + file_paths:
            if not os.path.exists(path):
                content += f"[File not found: {path}]\n"
            else:
                with open(path, "r") as f:
                    content += f.read()
        return content


class ColoredFileReader(FileReader):
    """FileReader with colored terminal output."""

    @color_decorator("blue")
    def __str__(self):
        """Return file contents with blue color."""
        return super().__str__()

    @color_decorator("red")
    def concat_files(self, *file_paths):
        """Concatenate files with red color."""
        result = super().concat_files(*file_paths)
        return f"--- Concatenated Content ---\n{result}"

    @color_decorator("blue")
    def read_lines(self):
        """Return file lines as list with blue color."""
        return [line for line in super().read_lines()]


if __name__ == "__main__":
    # Basic usage
    fr1 = FileReader("file1.txt")
    fr2 = FileReader("file2.txt")
    print(fr1)
    print(fr1 + fr2)
    print("\n")
    print("Now we use the color decorator")
    print("Fahad thinks its funny and helps us look at it better\n\n")
    # Color usage
    cfr = ColoredFileReader("file1.txt")
    print(cfr)
    print(cfr.concat_files("file2.txt", "file3.txt"))
