from lettuce import *
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os

def find_field_by_class(browser, attribute):
    xpath = "//input[@class='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False

@step('I fill in field with class "(.*?)" with "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
    with AssertContextManager(step):
        text_field = find_field_by_class(world.browser, field_name)
        text_field.clear()
        text_field.send_keys(value)

@step('I go to "(.*?)"')
def open_url(self, url):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(3) 
    self.driver.get(url + "/")

#def open_browser(url):
#    driver = webdriver.Firefox()
#    driver.implicitly_wait(3)
#    driver.get(url + "/")
       
