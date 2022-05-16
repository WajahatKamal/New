import os
import json
from pluggy import HookspecMarker

hookspec = HookspecMarker("pytest")


class UserData(object):
    """Simple singleton class for managing and accessing user test data"""

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\testdata", 'test_user_data.json')) as f:
            setting = json.load(f)
            self.userName = setting['userName']
            self.password = setting['password']
            self.firstname = setting['firstname']
            self.lastname = setting['lastname']
            self.emailinvite = setting['emailinvite']


userData = UserData()
