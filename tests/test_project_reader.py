
from project_reader import read_project


def test_missing_file():
    read_project('missing.csv')