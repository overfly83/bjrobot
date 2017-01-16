#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pywinauto.application import Application

app =  Application().connect(process=19528)
print app.top_window().print_control_identifiers()
