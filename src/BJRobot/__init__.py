import os
from keywords import *
from utilities import System
from version import VERSION

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))

__version__ = VERSION



class BJRobot(BrowserManager, Element, Screenshot, Logging, RunOnFailure):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self,
                 run_on_failure='Capture Page Screenshot',
                 screenshot_root_directory=None
                 ):
        for base in BJRobot.__bases__:
            base.__init__(self)

        self.screenshot_root_directory = screenshot_root_directory
        self.register_keyword_to_run_on_failure(run_on_failure)
