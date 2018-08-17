#!/usr/bin/env python 
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import HTMLTestRunner #引入 HTMLTestRunner 包
import os


# this, self


# left = Light()

# left.open()
# left.close()
# left.status

# right = Light()

# right.open()
# right.close()
# right.status



class LilyWeb:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)

    def open_url(self, url):

        base_url = "http://www.baidu.com/"
        # self.driver = self.driver
        self.driver.get(base_url + "/")
        self.driver.find_element_by_id("kw").send_keys("selenium webdriver")
        self.driver.find_element_by_id("su").click()
        #time.sleep(2)
        # self.driver.close()

    def click_button(self, element_location):
        self.driver.find_element_by_css_selector(element_location).click()

        pass

    def exit(self):
        self.driver.close()

if __name__ == "__main__":
    url = "http://www.baidu.com/"
    test = LilyWeb()
    # again = LilyWeb()

    # test.driver  again.driver
    # * I goto page xxxxx
    result = test.open_url(url)
    test.click_button(".s_tab_inner > a:nth-child(6)")
