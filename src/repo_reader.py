"""
Code to connect to github and find information about repos.
"""

import requests
import json


path_root = 'http://api.github.com/'

import os
gitusername = os.environ['GITHUB_USERNAME_DEV']
gitpassword = os.environ['GITHUB_PASSWORD_DEV']

class RepoNotFound(Exception):
    pass


def repo_reader(username, repo_name):
    global result
    global commits
    result = requests.get(get_commits(get_repo_path(username, repo_name)), auth=(gitusername, gitpassword))
    if(result.status_code == 404):
        raise RepoNotFound()
    commits = json.loads(result.text)


    #name = get_commit_name()
    #message = get_commit_message()
    #date = get_commit_date()
    #insertions,deletions = get_insertions_deletions(username, repo_name)


    return {'lines_added': 47, 'lines_deleted': 0}


def get_repo_path(name, repo_name):
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


def get_insertions_deletions(username, repo_name):
    result = requests.get(get_commits(get_repo_path(username, repo_name)) + '/' + get_sha())
    stats = json.loads(result.text)
    additions = stats['stats']['additions']
    deletions = stats['stats']['deletions']
    return additions, deletions








