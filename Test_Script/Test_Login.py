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








