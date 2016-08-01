from selenium import webdriver
from base import Page
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import os
import time

class HomePage(Page):

    def click_become_top_button(self):
        self.find_element(*HomePageLocators.BECOME_TOP_BUTTON).click()
        return RegisterPage(self.driver)

class RegisterPage(Page):

    def enter_firstname(self, firstname):
        self.find_element(*FormPageBecomeInstructor.FIRST_NAME).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.find_element(*FormPageBecomeInstructor.LAST_NAME).send_keys(lastname) 

    def enter_email(self, email):
        self.find_element(*FormPageBecomeInstructor.EMAIL).send_keys(email)
    
    def enter_password(self, password):
        self.find_element(*FormPageBecomeInstructor.PASSWORD).send_keys(password) 

    def enter_phone(self, phone):
        self.find_element(*FormPageBecomeInstructor.PHONE).send_keys(phone)

    def accept_terms(self):
        self.find_element(*FormPageBecomeInstructor.TERMS).click()    

    def click_submit_form(self):
        self.find_element(*FormPageBecomeInstructor.SUBMIT_FORM_BUTTON).click()

    def click_submit_question(self):
        self.find_element(*FormPageBecomeInstructor.SUBMIT_BUTTON_QUESTION_PAGE).click()
        return self.find_element(*FormPageBecomeInstructor.SUCCESS_MESSAGE).text

    def register_valid_user(self):
        self.enter_firstname("rafael")
        self.enter_lastname("carvalho")
        self.enter_email("rafaelcrvs@gmail.com")
        self.enter_password("12345678")
        self.enter_phone("12345678910")
        dropdown_city = self.driver.find_element_by_name("city")
        self.driver.execute_script('arguments[0].removeAttribute("disabled");', dropdown_city)        
        mySelect = Select(self.driver.find_element_by_name("city"))
        mySelect.select_by_value("Shanghai")
        certificate_field = self.driver.find_element_by_name("qualification2")
        self.driver.execute_script('arguments[0].removeAttribute("class"); arguments[0].style["margin-left"] = 0;', certificate_field)
        certificate_file = os.path.abspath("tests/certificate.jpeg/")
        certificate_field.send_keys(certificate_file)
        time.sleep(5)
        self.accept_terms()
        self.click_submit_form()
        time.sleep(10)
        success_message = self.click_submit_question()
        time.sleep(5)
        assert success_message == "Get Verified"

class LoginAdmin(Page):

    def enter_email_admin(self, email_admin):
        self.find_element(*LoginSuperAdmin.EMAIL_ADMIN).send_keys(email_admin)

    def enter_password_admin(self, password_admin):
        self.find_element(*LoginSuperAdmin.PASSWORD_ADMIN).send_keys(password_admin)

    def click_login_admin(self):
        self.find_element(*LoginSuperAdmin.LOGIN_BUTTON_ADMIN).click()

    def login_with_admin(self, email_admin, password_admin):
        self.enter_email_admin(email_admin)
        self.enter_password_admin(password_admin)
        self.click_login_admin()
        #return self.find_element(*LoginSuperAdmin.LOGOUT_CLASS)

class DeleteTrainers(Page):

    def click_trainers_menu(self):
        self.find_element(*Admin_LocatorsTrainers.TRAINERS_MENU).click()     

    def click_edit_button(self):
        self.find_element(*Admin_LocatorsTrainers.EDIT_BUTTON).click()

    def click_delete_trainer_button(self):
        self.find_element(*Admin_LocatorsTrainers.DELETE_TRAINER_BUTTON).click()

    def delete_all_trainers(self):        
        while True:
            try:
                self.click_trainers_menu()
                self.click_edit_button()
                self.click_delete_trainer_button()
                alert = self.driver.switch_to_alert()
                alert.accept()
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "container-fluid")))
            except NoSuchElementException:
                self.driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "t")
                self.driver.get("http://dev.letsfiti.com/")
                break
