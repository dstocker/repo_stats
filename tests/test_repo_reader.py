from repo_reader import *
import pytest
import requests_mock
import json


def test_setup():
    set_dict({'JohnSpp':'repo_stats'})
    repo_reader()
    # commits = json.loads(result.text)


def test_path():
    assert(get_repo_path('JohnSpp') == 'http://api.github.com/repos/JohnSpp/repo_stats')


def test_commit_path():
    assert (get_commits(get_repo_path('JohnSpp')) == 'http://api.github.com/repos/JohnSpp/repo_stats/commits')


def test_connect():
    result = requests.get(get_commits(get_repo_path('JohnSpp')))
    assert (result.status_code == 200)


def test_commit():
    assert (get_commit_name() == "Alex Haug")


def test_message():
    assert (get_commit_message() == "Merge pull request #1 from bjcoleman/master\n\nCreate Read Project and Tests (initial work)")


def test_get_date():
    assert (get_commit_date() == '2018-05-31T19:58:40Z')


def test_sha():
    assert (get_sha() == '6f6b5f9334e61e5cc49c81897f40c61ec6ca86c2')


def test_get_insertions():
    x, y = get_insertions_deletions()
    assert ( x == 47)
    assert (y == 0)


