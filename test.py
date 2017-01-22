#!/usr/bin/python
# -*- coding: UTF-8 -*-
from BJRobot import *

aa = BJRobot()

try:
    aa.open_browser("http://www.bing.com")

    aa.open_new_window("http://www.baidu.com")
    aa.switch_window(u"百度一下， 你就知道")
    aa.set_value('id=kw','test')
    aa.set_value_by_id('kw','test')
    aa.click_element('id=su')
    aa.click_element_by_id('su')
    aa.find_element('partial link text=JavaScript')
    aa.find_element_by_partial_link_text('JavaScript')
    aa.switch_window_contains("bing.com")
    aa.set_value('id=sb_form_q', 'test')
    aa.set_value_by_id('sb_form_q','test')
    aa.click_element('id=sb_form_go')
    aa.click_element_by_id('sb_form_go')
    aa.find_element_by_xpath("//li[@class='b_ans' and @data-bm='7']")
    aa.find_element("xpath=//li[@class='b_ans' and @data-bm='7']")
    # print aa.is_element_present("id=ddd", timeout=1)
    aa.close_browser()


    aa.open_application('http://127.0.0.1:4723/wd/hub', platformName='Android', platformVersion='4.2.2', deviceName='tesddt', app='e:/robotframework-appiumlibrary/demo/demoapp/ContactManager.apk', automationName='appium')
    aa.click_element_m('id=com.example.android.contactmanager:id/addContactButton')
    aa.input_text_m('id=com.example.android.contactmanager:id/contactNameEditText', 'appium user')
    aa.input_text_m('id=com.example.android.contactmanager:id/contactPhoneEditText', '55554446666')
    aa.input_text_m('id=com.example.android.contactmanager:id/contactEmailEditText', 'demo@io.com')
    aa.click_element_m('accessibility_id=Save')
    aa.close_application()

finally:
    aa.close_all_browsers()
    aa.close_all_applications()

# python -m robot.libdoc -f html BJRobot e:/bjrobot/doc/BJRobot.html


