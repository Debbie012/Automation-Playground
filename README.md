# Automation-Playground
This project automates key features of the Automation Playground CRM using Selenium with Python.

✅ Automated Features
Login Page: Automates login using valid credentials.

Homepage: Clicks the "Add Customer" button after successful login.

Add Customer Form: Fills and submits the form with test data.

Logout: Automates logout after adding a customer.

# Setting up POM
Create virtual environment 
Click Python version at the bottom right of Pycharm
Click on Add New Interpreter
Click Local Interpreter
Click OK

Create a requirements.txt file
Open Pycharm Terminal
Use the Commandline below to install requirements.txt 

-pip install -r requirements.txt
-pip  freeze
-pip  freeze > requirements.txt

Use the Commandline below to Install Selenium 
pip install selenium

Use the Commandlines below to install two Python packages
pip install selenium pytest
pip install pytest-html

✅ 1. selenium
A browser automation framework.
Allows you to control web browsers through programs for testing web applications.
Often used in automated UI testing.

✅ 2. pytest
A powerful testing framework for Python.
Used for writing and running unit tests, functional tests, or even end-to-end tests.

My_Selenium_Project/
│
├── locators/
│   └── login_locators.py
│
├── actions/
│   └── login_actions.py
│
├── tests/
│   └── test_login.py
│
├── requirements.txt
└── conftest.py (for pytest setup, if using pytest)

# LocatorsPage
from selenium.webdriver.common.by import By

class LoginLocators:
      Input_Email = (By.ID, "email-id")
      Input_Password = (By.ID, "password")
      Remember_me_Checkbox = (By.ID, "remember")
      Submit_Button = (By.ID, "submit-id")

class HomePageLocators:
      Add_Customer = (By.ID, "new-customer")

class CustomerFormLocators:
      Input_Email = (By.ID, "EmailAddress")
      Input_FirstName = (By.ID, "FirstName")
      Input_LastName = (By.ID, "LastName")
      Input_City = (By.ID, "City")
      State = (By.ID, "StateOrRegion")
      # Select_State = (By.XPATH, "//*[@id=StateOrRegion]/option[11]")
      Select_Gender = (By.CSS_SELECTOR, "input[name='gender'][value='female']")
      Add_To_Promotional_List = (By.CSS_SELECTOR, "input[name='promos-name']")
      Submit = (By.CSS_SELECTOR, "button[type='submit']")

class SignOutLocators:
      SignOut = (By.XPATH, "/html/body/nav/ul/li/a")

# ActionPage
import time
from selenium.webdriver.support.ui import WebDriverWait

from Config.configuration import Config
from Locators.Login_Page import LoginLocators, HomePageLocators, CustomerFormLocators, SignOutLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(Config.WAIT_TIME)

    def open_login_page(self,url):
        self.driver.get(url)
        time.sleep(Config.WAIT_TIME)

    def email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Input_Email))
        enter_email_address.send_keys(email_address)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Input_Password))
        enter_password.send_keys(password)

    def remember_me(self):
        remember_me = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Remember_me_Checkbox))
        remember_me.click()

    def submit(self):
        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.Submit_Button))
        submit_button.click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(Config.WAIT_TIME)

    def new_customer(self):
        add_customer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(HomePageLocators.Add_Customer))
        add_customer.click()

class CustomerForm:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(Config.WAIT_TIME)

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Input_Email))
        enter_email.send_keys(email)

    def first_name(self, first_name):
        enter_first_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Input_FirstName))
        enter_first_name.send_keys(first_name)

    def last_name(self, last_name):
        enter_last_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Input_LastName))
        enter_last_name.send_keys(last_name)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Input_City))
        enter_city.send_keys(city)

    def enter_state(self, state):
        enter_state = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.State))
        enter_state.send_keys(state)

    #def select_state(self):
    #    select_state = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Select_State))
     #   select_state.click()

    def select_gender(self):
        select_gender = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Select_Gender))
        select_gender.click()

    def add_to_promo_list(self):
        add_to_promo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Add_To_Promotional_List))
        add_to_promo.click()

    def submit(self):
        submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.Submit))
        submit.click()

class SignOut:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(Config.WAIT_TIME)

    def sign_out(self):
        sign_out = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(SignOutLocators.SignOut))
        sign_out.click()

# TestScript
import pytest
from selenium import webdriver

from Action.Action_Page import LoginPage, HomePage, CustomerForm, SignOut
from Config.configuration import Config


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

def test_login_page_on_automation_playground(login):
    login.email_address(Config.EMAIL_ADDRESS)
    login.password(Config.PASSWORD)
    login.remember_me()
    login.submit()

def test_add_new_customer_on_automation_playground(login):
    add_customer = HomePage(login.driver)
    add_customer.new_customer()

def test_customer_form_on_automation_playground(login):
    customer_form = CustomerForm(login.driver)
    customer_form.email(Config.ENTER_EMAIL)
    customer_form.first_name(Config.FIRST_NAME)
    customer_form.last_name(Config.LAST_NAME)
    customer_form.city(Config.CITY)
    customer_form.enter_state(Config.STATE)
    # customer_form.select_state(Config.STATE)
    customer_form.select_gender()
    customer_form.add_to_promo_list()
    customer_form.submit()

def test_sign_out_on_automation_playground(login):
    sign_out = SignOut(login.driver)
    sign_out.sign_out()

# ConfigPage
class Config:
      BASE_URL = "https://automationplayground.com/crm/login.html"
      EMAIL_ADDRESS = "eddy@yopmail.com"
      PASSWORD = "cloud"
      ENTER_EMAIL = "eddy@yopmail.com"
      FIRST_NAME = "Joshua"
      LAST_NAME = "Alex"
      CITY = "Lagos"
      STATE = "Maryland"
      WAIT_TIME = 5






