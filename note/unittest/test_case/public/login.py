#!/usr/bin/env python 
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Baidu(unittest.TestCase):
	
    def setUp(self):
        self.driver = webdriver.Firefox()
	self.driver.implicitly_wait(30)
	self.base_url = "http://www.baidu.com/"
	self.verificationErrors = []
	self.accept_next_alert = True

	#百度搜索用例
    def test_baidu_search(self):
	driver = self.driver
	driver.get(self.base_url + "/")
	driver.find_element_by_id("kw").send_keys("selenium webdriver")
	driver.find_element_by_id("su").click()
	time.sleep(2)
	driver.close()

    def tearDown(self):
	self.driver.quit()
	self.assertEqual([], self.verificationErrors)
	print "success with baidu.py"

if __name__ == "__main__":
    unittest.main()
