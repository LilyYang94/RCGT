from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['version'] = ''
    desired_capabilities['platform'] = 'ANY'
    desired_capabilities['browserName'] = 'firefox'
    desired_capabilities['avascriptEnabled'] = True

  #  world.browser = webdriver.Remote(
   #     desired_capabilities=desired_capabilities,
   #     command_executor="http://127.0.0.1:4444/wd/hub")
