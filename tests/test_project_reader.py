
from project_reader import read_project
import pytest
PATH = 'tests/test_files/'


def test_missing_file():
    with pytest.raises(FileNotFoundError): read_project(PATH + 'missing.csv')


def test_empty_file():
    assert read_project(PATH + 'empty.csv') == []


def test_read_one_line():
    assert read_project(PATH + 'one.csv') == [{'Sam Mai Tai':'foo'}]


def test_read_many_lines():
    assert read_project(PATH + 'many.csv') == [{'Sam Mai Tai': 'foo'},
                                               {'Morbid Mojito': 'bar'},
                                               {'James Brandy': 'python'}]


def test_only_username():
    assert read_project(PATH + 'onlyusername.csv') == []


def test_only_reponame():
    assert read_project(PATH + 'onlyreponame.csv') == []


def test_only_username_bad_format():
    assert read_project(PATH + 'onlyusernamebadformat.csv') == []


def test_many_bad_format():
    assert read_project(PATH + 'manybadformat.csv') == [{'Sam Mai Tai': 'foo'},
                                               {'Morbid Mojito': 'bar'},
                                               {'James Brandy': 'python'}]
