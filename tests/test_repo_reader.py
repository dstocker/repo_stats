from repo_reader import *
import pytest
import requests_mock

def test_setup():
    set_dict({'JohnSpp':'repo_stats'})

def test_path():
    assert(get_repo_path('JohnSpp') == 'http://api.github.com/repos/JohnSpp/repo_stats')

def test_commit_path():
    assert (get_commits(get_repo_path('JohnSpp')) == 'http://api.github.com/repos/JohnSpp/repo_stats/commits')

