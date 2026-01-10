from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver= driver
        self.__usernameTxtBx = "//input[@name='email']"
        self.__passwordTxtBx = "//input[@name='pass']"
        self.__loginBtn = "//button[@name='login']"


    def enter_user_credentials(self, username, password):
        self.driver.find_element(By.XPATH, self.__usernameTxtBx).send_keys(username)
        self.driver.find_element(By.XPATH, self.__passwordTxtBx).send_keys(password)


    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.__loginBtn).click()
