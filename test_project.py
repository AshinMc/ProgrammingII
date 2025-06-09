import os
import pytest
from project import FileReader, ColoredFileReader

# Create test files
@pytest.fixture
def setup_files():
    with open("test_file1.txt", "w") as f:
        f.write("Content of file 1")
    with open("test_file2.txt", "w") as f:
        f.write("Content of file 2")
    yield
    # Clean up
    os.remove("test_file1.txt")
    os.remove("test_file2.txt")

def test_file_reader_init():
    reader = FileReader("test_path.txt")
    assert reader.file_path == "test_path.txt"

def test_property_setter():
    reader = FileReader("old_path.txt")
    reader.file_path = "new_path.txt"
    assert reader.file_path == "new_path.txt"

def test_file_exists_static_method():
    assert FileReader.file_exists("non_existent_file.txt") == False

def test_from_directory_class_method():
    reader = FileReader.from_directory(".", "file.txt")
    assert reader.file_path == "./file.txt"

def test_read_lines(setup_files):
    reader = FileReader("test_file1.txt")
    lines = list(reader.read_lines())
    assert lines == ["Content of file 1"]

def test_concatenation(setup_files):
    fr1 = FileReader("test_file1.txt")
    fr2 = FileReader("test_file2.txt")
    result = fr1 + fr2
    assert "Content of file 1" in result
    assert "Content of file 2" in result