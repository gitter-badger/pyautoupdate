import requests
import pytest

def has_internet():
    '''Uses 8.8.8.8 to check connectivity'''
    try:
        requests.head('http://www.google.com', timeout=1)
        return True
    except requests.ConnectionError:
        return False

needinternet=pytest.mark.skipif(not has_internet(), reason="This test needs internet")