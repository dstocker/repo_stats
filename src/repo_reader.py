"""
Code to connect to github and find information about repos.
"""

import requests
import json


dict = {'JohnSpp':'repo_stats'}
path_root = 'http://api.github.com/'

import os
username = os.environ['GITHUB_USERNAME_DEV']
password = os.environ['GITHUB_PASSWORD_DEV']


def repo_reader():
    global result
    global commits
    result = requests.get(get_commits(get_repo_path('JohnSpp')), auth=(username, password))
    commits = json.loads(result.text)


    name = get_commit_name()
    message = get_commit_message()
    date = get_commit_date()
    insertions,deletions = get_insertions_deletions()
    
    #print("Name: " + name + '\n' + "Message: " + message + '\n' + "Date: " +date + '\n' + "Insertions: " + str(insertions) + '\n'
     #     + "Deletions: " + str(deletions) + '\n')



def set_dict(new_dict):
    global dict
    dict = new_dict


def get_repo_path(name):
    repo_name = dict.get(name)
    return path_root + 'repos/' + name + '/' + repo_name


def get_commits(repo_path):
    return repo_path + '/commits'


def get_commit_name():
    return commits[0]['commit']['author']['name']


def get_commit_message():
    return commits[0]['commit']['message']


def get_commit_date():
    return commits[0]['commit']['committer']['date']


def get_sha():
    return commits[0]['sha']


def get_insertions_deletions():
    result = requests.get(get_commits(get_repo_path('JohnSpp')) + '/' + get_sha())
    stats = json.loads(result.text)
    additions = stats['stats']['additions']
    deletions = stats['stats']['deletions']
    return additions, deletions







repo_reader()

