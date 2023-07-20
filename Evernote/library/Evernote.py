import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
path_c = str(Path(os.getcwd()).parent.parent)
sys.path.append(os.path.join(str(path_c), "alphabin\\map"))
sys.path.append(str(path_c + '\\alphabin'))
sys.path.append(str(path_c) + "alphabin\\common_utilities\\")
from common_functionality import *
#from map import Signup as map
from Signup import Signup
from Home import Home
from Task import Task
from Login import Login


class Evernote(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.driver = WebDriver()
        self.signup = Signup(self.driver)
        self.login = Login(self.driver)
        self.home = Home(self.driver)
        self.task = Task(self.driver)



