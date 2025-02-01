'''Test Requirements:
	•	Write to a temporary file and verify the content matches.
	•	Test for invalid filenames (e.g., empty strings or restricted characters).
	•	Test edge cases like writing/reading an empty string.
	•	Ensure exceptions are raised if reading a non-existent file.
'''

import pytest
from exercise5.source import write_to_file, read_from_file
import os
import sys

CONTENT_BEFORE_TEST = "Before test"
CONTENT_AFTER_TEST = "After test"
TEST_FILE_NAME = "test_file.txt"


#checks if function creates a file
def test_write_to_file_creation(tmp_path):
    temp_directory = tmp_path / "sub"
    temp_directory.mkdir()
    assert len(list(temp_directory.iterdir())) == 0
    write_to_file(temp_directory / TEST_FILE_NAME, CONTENT_AFTER_TEST)
    assert len(list(temp_directory.iterdir())) == 1

#checks if the name of created file
def test_write_to_file_filename(tmp_path):
    temp_directory = tmp_path / "sub"
    temp_directory.mkdir()
    test_file_path = temp_directory / TEST_FILE_NAME
    write_to_file(test_file_path, CONTENT_AFTER_TEST)
    assert test_file_path.exists()
    assert os.path.basename(test_file_path) == TEST_FILE_NAME


@pytest.mark.parametrize("file_name", ["?", ">", "<", ":", "'", "/", "\\", "|", "?", "*"])
@pytest.mark.skipif(sys.platform != "win32", reason = "filename restrictions are OS-specific")
def test_write_to_file_improper_name(tmp_path, file_name):
    temp_directory = tmp_path / "sub"
    temp_directory.mkdir()
    with pytest.raises(OSError):
        write_to_file(temp_directory / file_name, CONTENT_AFTER_TEST)


def test_write_to_file_writing(tmp_path):
    temp_directory = tmp_path / "sub"
    temp_directory.mkdir()
    temp_file = temp_directory / TEST_FILE_NAME
    temp_file.write_text(CONTENT_BEFORE_TEST)
    write_to_file(temp_file, CONTENT_AFTER_TEST)
    assert temp_file.read_text() != CONTENT_BEFORE_TEST + CONTENT_AFTER_TEST
    assert temp_file.read_text() == CONTENT_AFTER_TEST


def test_read_from_file_no_file(tmp_path):
    non_existent_file = tmp_path / "non_existent.txt"
    with pytest.raises(FileNotFoundError):
        read_from_file(non_existent_file)


def test_read_from_file(tmp_path):
    temp_directory = tmp_path / "sub"
    temp_directory.mkdir()
    file_path = temp_directory / TEST_FILE_NAME
    file_path.write_text(CONTENT_AFTER_TEST)
    assert read_from_file(file_path) == CONTENT_AFTER_TEST


def test_read_from_file_empty_string(tmp_path):
    temp_directory = tmp_path / "sub"
    temp_directory.mkdir()
    temp_file_patch = temp_directory / TEST_FILE_NAME
    temp_file_patch.write_text("")
    assert read_from_file(temp_file_patch) == ""


def test_read_binary_file(tmp_path):
    temp_file = tmp_path / "binary_file.bin"
    temp_file.write_bytes(b'\x00\xFF\xAA')
    assert read_from_file(temp_file) == b'\x00\xFF\xAA'

