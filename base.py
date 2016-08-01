from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Page(object):
    def __init__(self, driver, base_url='https://domain.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
 
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
 
    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
    
    """
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
    """