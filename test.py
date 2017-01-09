#!/usr/bin/python
# -*- coding: UTF-8 -*-
from BJRobot import *
import time

aa = BJRobot()

aa.open_browser("http://www.bing.com")
time.sleep(15)
aa.switch_window(u"百度一下， 你就知道")
aa.set_value('id','kw','test')
aa.click_element_by_id('su')
aa.find_element_by_partial_link_text('JavaScript')
aa.switch_window_contains("bing.com")
aa.set_value_by_id('sb_form_q','test')
aa.click_element_by_id('sb_form_go')
aa.find_element_by_xpath("//li[@class='b_ans' and @data-bm='7']")
time.sleep(5)
aa.close_browser()
