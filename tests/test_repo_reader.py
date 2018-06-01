# from repo_reader import *
# import pytest
# import requests
# import requests_mock
# import json
#
#
# adapter = requests_mock.Adapter()
# session = requests.Session()
# session.mount('http', adapter)
#
#
#
# # adapter.register_uri('GET', 'http://api.github.com/repos/JohnSpp/repo_stats', status_code=200)
#
#
#
# def test_setup():
#     repo_reader('JohnSpp', 'repo_stats')
#     # commits = json.loads(result.text)
#
#
# def test_path():
#     assert(get_repo_path('JohnSpp', 'repo_stats') == 'http://api.github.com/repos/JohnSpp/repo_stats')
#
#
# def test_commit_path():
#     assert (get_commits(get_repo_path('JohnSpp', 'repo_stats')) == 'http://api.github.com/repos/JohnSpp/repo_stats/commits')
#
#
# def test_connect():
#
#     with requests_mock.Mocker() as m:
#         m.get('http://api.github.com/repos/JohnSpp/repo_stats', text='{}')
#         assert repo_reader('JohnSpp', 'repo_stats') == "AA"
#     #adapter.register_uri('GET', 'http://api.github.com/repos/JohnSpp/repo_stats', status_code=200)
#     #result = session.get(get_commits(get_repo_path('JohnSpp')))
#         # requests.get(get_commits(get_repo_path('JohnSpp')))
#     #assert (result.status_code == 200)
#
#
# def test_commit():
#     assert (get_commit_name() == "Alex Haug")
#
#
# def test_message():
#     assert (get_commit_message() == "Merge pull request #1 from bjcoleman/master\n\nCreate Read Project and Tests (initial work)")
#
#
# def test_get_date():
#     assert (get_commit_date() == '2018-05-31T19:58:40Z')
#
#
# def test_sha():
#     assert (get_sha() == '6f6b5f9334e61e5cc49c81897f40c61ec6ca86c2')
#
#
# def test_get_insertions():
#     x, y = get_insertions_deletions('JohnSpp', 'repo_stats')
#     assert ( x == 47)
#     assert (y == 0)

import requests_mock
import pytest
from repo_reader import *



def test_bad_username_throws_exception():

    with requests_mock.Mocker() as m:
        m.get('http://api.github.com/repos/bjcoleman/foo/commits',
              status_code=404)
        with pytest.raises(RepoNotFound):
            repo_reader('bjcoleman', 'foo')


def test_happy_path():

    with open('tests/test_files/commitexample.json') as f:
        expected_json = f.read()

        with requests_mock.Mocker() as m:
            m.get('http://api.github.com/repos/bjcoleman/foo/commits', text=expected_json)

            expected_results = {'lines_added': 47, 'lines_deleted': 0}

            assert repo_reader('bjcoleman', 'foo') == expected_results


