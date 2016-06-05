from __future__ import absolute_import, print_function

from ..pyautoupdate.launcher import Launcher
from .pytest_skipif import needinternet
from .pytest_makevers import fixture_update_dir

import os

@needinternet
def test_check_vers_update(fixture_update_dir):
    package=fixture_update_dir("0.0.1")
    launch = Launcher('',r'http://rlee287.github.io/pyautoupdate/testing/')
    launch._get_new()
    with open(os.path.abspath("downloads/blah.py"), "r") as file_code:
        file_text=file_code.read()
    assert "new version" in file_text