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



