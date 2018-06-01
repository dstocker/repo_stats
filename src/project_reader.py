import csv

"""
Code to read the list of username and repo names from a CSV file.
"""


def read_project(filename):
    """
    Read the projects from a CSV file.

    The fields of the file are username and repo name

    Ignores entries where username or repo name is blank.

    :param filename: the path of the file to read (relative to package)
    :return: list of dicts (username,repo_name)
    :raises: FileNotFoundError if the file cannot be opened
    """

    with open(filename) as csvfile:
        list = []
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                if row[0] != "" and row[1] != "":
                    dict = {row[0]: row[1]}
                    list.append(dict)
            except IndexError:
                pass

    return list
