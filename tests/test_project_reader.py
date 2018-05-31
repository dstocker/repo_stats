
from project_reader import read_project
import pytest


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        read_project('missing.csv')


def test_empty_file():
    assert read_project('tests/test_files/empty.csv') == []