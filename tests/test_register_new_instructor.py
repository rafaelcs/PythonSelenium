import pytest
import os
from selenium import webdriver
from page import *
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class TestRegisterNewInstructor:

    def setup_class(cls):
        cls.driver = webdriver.Chrome('./chromedriver')
        cls.driver.get("https://domain.com/")
        cls.driver.maximize_window()

    def test_01_LoginWithAdmin(self):

        loginPage = LoginAdmin(self.driver)
        loginPage.login_with_admin("username@gmail.com", "12345")

    def teardown_class(cls):
        cls.driver.close()


