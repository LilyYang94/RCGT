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

class Baidu(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
	u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    #百度设置用例
    def test_baidu_set(self):
	u"""百度设置"""
        driver = self.driver
        #进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")
        #设置每页搜索结果为 20 条
        m=driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='20']").click()
        time.sleep(2)
        #保存设置的信息
        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "success with baidu.py"


#if __name__ == "__main__":
#
#    testunit = unittest.main()
#    #定义一个单元测试容器
#    # testunit=unittest.TestSuite()
#
#    #将测试用例加入到测试容器中
#    #testunit.addTest(Baidu("test_baidu_search"))
#    #testunit.addTest(Baidu("test_baidu_set"))
#
#    #定义个报告存放路径,支持相对路径
#    filename = './report/result.html'
#    print os.path.abspath(filename)
#    fp = file(filename, 'wb')
#
#    #定义测试报告
#    runner =HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况:')
#    print runner
#
#    #运行测试用例
#    runner.run(testunit)


if __name__ == "__main__":
    unittest.main()
