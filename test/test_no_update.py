from __future__ import absolute_import, print_function

from ..pyautoupdate.launcher import Launcher
from .pytest_skipif import needinternet
from .pytest_makevers import fixture_update_dir

import os

@needinternet
def test_check_vers_noupdate(fixture_update_dir):
    """Tests that check that updates do not occur when unnecessary"""
    package=fixture_update_dir('0.2.0')
    launch = Launcher('pypipypipypipypi',
                      r'http://rlee287.github.io/pyautoupdate/testing/')
    isnew=launch.update_code()
