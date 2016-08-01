from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage(Page):

    def check_instructor_form_page_loaded(self):
        return True if self.find_element(*FormPageBecomeInstructor.SUBMIT_FORM_BUTTON) else False

    def click_become_top_button(self):
        self.find_element(*HomePageLocators.BECOME_TOP_BUTTON).click()

    def click_become_bottom_button(self):
        self.find_element(*HomePageLocators.BECOME_BOTTOM_BUTTON).click()

    