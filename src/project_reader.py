
"""
Code to read the list of username and repo names.
"""


def read_project(filename):
    """
    Read the projects from a CSV file.

    The fields of the file are username and repo name
    :param filename: the path of the file to read (relative to package)
    :return: list of dicts (username,repo_name)
    :raises: FileNotFoundError if the file cannot be opened
    """

    with open(filename) as f:
        pass

    return []
