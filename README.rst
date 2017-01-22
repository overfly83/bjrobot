Introduction
--------------
RJRobot is an webdriver based testing library for RobotFramework which could handle both desktop browser and mobile native and hybrid app.

It support latest Selenium 3.0 webdriver and could be used without downloading webdriver for each browser again.
It uses Appium (version 1.x) to communicate with Android and iOS application similar to how Selenium WebDriver talks to web browser.

It support Python 2.x for now.



Installation
-------------

Using ``pip``
'''''''''''''

The recommended installation method is using
`pip <http://pip-installer.org>`__::

    pip install robotframework-bjrobot

The main benefit of using ``pip`` is that it automatically installs all
dependencies needed by the library. Other nice features are easy upgrading
and support for un-installation::

    pip install -U robotframework-bjrobot
    
    pip uninstall robotframework-bjrobot




Directory Layout
------------------------
doc/

Keyword documentation
src/

Python source code


Usage
-------------

To write tests with Robot Framework and BJRobot, BJRobot must be imported into your RF test suite. See   `Robot Framework User Guide <http://robotframework.org/robotframework/#user-guide>`_ for more information.

As it uses Appium make sure your Appium server is up and running. For how to use Appium please refer to Appium Documentation


Documentation
---------------
The keyword documentation could be found at `Keyword Documentation <https://overfly83.github.io/BJRobot.html>`_ 


TO LIST
----------

execute_javascript

shell command support

Desktop GUI Automation
