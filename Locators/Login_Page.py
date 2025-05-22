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






