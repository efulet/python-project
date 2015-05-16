"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import pytest

from ..lib.util.file_utils import FileUtils


def test_no_path():
    with pytest.raises(Exception) as excinfo:
        FileUtils().do_path()
    assert excinfo.value.message == "There is no paths to join"

def test_do_path():
    t0_path = "/tmp/test.txt"
    t1_path = FileUtils().do_path(["/tmp","test.txt"])
    assert t0_path == t1_path

def test_log_path():
    t0_path = "lib/util/../../../log"
    t1_path = FileUtils().log_path()
    assert True == (t0_path in t1_path)

def test_log_file():
    t0_path = "lib/util/../../../log/project.log"
    t1_path = FileUtils().log_file()
    assert True == (t0_path in t1_path)
