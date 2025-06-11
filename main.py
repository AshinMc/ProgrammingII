import os


def color_decorator(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "end": "\033[0m",
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors.get(color, colors['end'])}{result}{colors['end']}"

        return wrapper

    return decorator


class FileReader:
    def __init__(self, file_path):
        """Initialize with a file path."""
        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    def read_lines(self):
        if not os.path.exists(self._file_path):
            yield f"File not found: {self._file_path}"
            return

        with open(self._file_path, "r") as f:
            for line in f:
                yield line.rstrip("\n")

    @staticmethod
    def file_exists(path):
        return os.path.exists(path)

    @classmethod
    def from_directory(cls, directory, filename):
        return cls(os.path.join(directory, filename))

    def __str__(self):
        if not os.path.exists(self._file_path):
            return f"File not found: {self._file_path}"

        with open(self._file_path, "r") as f:
            return f.read()

    def __add__(self, other):
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
        content = ""
        for path in (self._file_path,) + file_paths:
            if not os.path.exists(path):
                content += f"[File not found: {path}]\n"
            else:
                with open(path, "r") as f:
                    content += f.read()
        return content


class ColoredFileReader(FileReader):

    @color_decorator("blue")
    def __str__(self):
        return super().__str__()

    @color_decorator("red")
    def concat_files(self, *file_paths):
        result = super().concat_files(*file_paths)
        return f"--- Concatenated Content ---\n{result}"

    @color_decorator("blue")
    def read_lines(self):
        return [line for line in super().read_lines()]


# Example usage
if __name__ == "__main__":
    # Basic FileReader usage
    fr1 = FileReader("file1.txt")
    fr2 = FileReader("file2.txt")
    print(fr1)
    print(fr1 + fr2)  # Using __add__
    print("\n")
    print("Now we use the color decorator")
    print("Fahad thinks its funny and helps us look at it better\n\n")
    # ColoredFileReader usage
    cfr = ColoredFileReader("file1.txt")
    print(cfr)
    print(cfr.concat_files("file2.txt", "file3.txt"))
