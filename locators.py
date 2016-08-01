from selenium.webdriver.common.by import By


class HomePageLocators(object):

  BECOME_TOP_BUTTON = (By.CSS_SELECTOR, '.rounded.btn.btn-white')
  SIGNUP_NEWSLETTER_BUTTON = (By.CSS_SELECTOR, '.signup-newsletter.uppercase.rounded.btn.btn-primary')
  BECOME_BOTTOM_BUTTON = (By.XPATH, "//a[contains(@href, '/en/signup')])[2]")

class FormPageBecomeInstructor(object):

  FIRST_NAME = (By.NAME, "first_name")
  LAST_NAME = (By.NAME, "last_name")
  EMAIL = (By.NAME, "email")
  PASSWORD = (By.NAME, "password")
  PHONE = (By.NAME, "phone")
  DROPDOWN_CITY = (By.NAME, "city")
  CHOOSE_CITY = (By.XPATH, "//label/ul/li")
  TERMS = (By.NAME, "terms")
  SUBMIT_FORM_BUTTON = (By.CSS_SELECTOR, ".submit.uppercase.rounded.btn.btn-block.btn-primary")
  SUBMIT_BUTTON_QUESTION_PAGE = (By.XPATH, "//button")
  SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".nextstep_card.nextstep_card1>h4")

class LoginSuperAdmin(object):

  EMAIL_ADMIN = (By.NAME, "username")
  PASSWORD_ADMIN = (By.NAME, "password")
  LOGIN_BUTTON_ADMIN = (By.LINK_TEXT, "Log in")

class Admin_LocatorsTrainers(object):

  TRAINERS_MENU = (By.CSS_SELECTOR, "li>a")
  EDIT_BUTTON = (By.XPATH, "//a[contains(text(),'Edit')]")
  DELETE_TRAINER_BUTTON = (By.CSS_SELECTOR, ".delete-trainer.btn.btn-primary.uppercase.rounded")
