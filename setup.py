#!/usr/bin/env python
from setuptools import setup
from os.path import abspath, join, dirname

CURDIR = dirname(abspath(__file__))
execfile(join(CURDIR, 'src', 'BJRobot', 'version.py'))

DESCRIPTION = """
BJRobot is a web testing library for Robot Framework
that leverages the Selenium 3 (WebDriver) libraries.
"""[1:-1]

with open(join(CURDIR, 'REQUIREMENTS.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(  
    name="robotframework-bjrobot",
    version=VERSION,
    package_dir={'': 'src'},
    packages=['BJRobot', 'BJRobot.keywords', 'BJRobot.utilities'],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    author="edward zhang",
    author_email="zhl830905@hotmail.com",
    platforms='any',
    description=DESCRIPTION,
    )   