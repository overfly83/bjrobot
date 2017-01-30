# -*- coding: utf-8 -*-

from keywords import *
from utilities import System
from version import VERSION

__version__ = VERSION


class BJRobot(BrowserManager, ApplicationManagemer, AndroidUtils, Keyevent,
              Touch, Element, Screenshot, Logging, RunOnFailure):
    """
    BJRobot is an webdriver based testing library for RobotFramework which could handle both
    desktop browser and mobile native and hybrid app.

    It support latest Selenium 3.0 webdriver and could be used without downloading webdriver for each browser again.
    It uses Appium (version 1.x) to communicate with Android and iOS application similar to how Selenium WebDriver
    talks to web browser.

    It support Python 2.x for now.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self,
                 run_on_failure='Capture Page Screenshot',
                 screenshot_root_directory=None
                 ):
        """BJRobot can be imported with optional arguments.
        ``run_on_failure`` specifies the name of a keyword (from any available
        libraries) to execute when a keyword fails.

        By default `Capture Page Screenshot` will be used to take a screenshot of the current page.
        Using the value `No Operation` will disable this feature altogether. See
        `Register Keyword To Run On Failure` keyword for more information about this
        functionality.

        Examples:
        | Library | BJRobot | run_on_failure=Capture Page Screenshot | # Capture the screenshot when on failure |
        | Library | BJRobot | run_on_failure=Capture Page Screenshot | screenshot root directory=../screenshot |
         #Capture screenshot on failure and set the log root directory to the screenshot above the current folder level
        """
        for base in BJRobot.__bases__:
            base.__init__(self)

        self.screenshot_root_directory = screenshot_root_directory
        self.register_keyword_to_run_on_failure(run_on_failure)
