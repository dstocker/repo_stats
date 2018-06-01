"""
Code to connect to github and find information about repos.
"""

import requests

dict = {}
path_root = 'http://api.github.com/'
def repo_reader():



    return

def set_dict(new_dict):
    global dict
    dict = new_dict

def get_repo_path(name):
    repo_name = dict.get(name)
    return path_root + 'repos/' + name + '/' + repo_name

def get_commits(repo_path):
    return repo_path + '/commits'





