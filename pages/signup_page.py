import time

from selenium.webdriver.common.by import By

from utils import base_utils


class SignupPage():
    def __init__(self, driver):
        self.driver= driver
        self.__header_text = "//img[@alt='Facebook']//..//following-sibling::div/div/div[1]"
        self.__firstname_textBox = "firstname"
        self.__secondname_textBox = "lastname"
        self.__first_name_error_message_icon = "//div[text()='First name']//parent::div[@class ='uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput']//following-sibling::i[1]"
        self.__surname_error_message_icon = "//div[text()='Surna']//parent::div[@class ='uiStickyPlaceholderInput uiStickyPlaceholderEmptyInpu']//following-sibling::i[1]"
        self.__firstname_error_message = "//div[text()='First name']//parent::div[@class ='uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput']//following-sibling::div/div"
        self.__surname_error_message = "//div[text()='Surname']//parent::div[@class ='uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput']//following-sibling::div/div"

    def get_page_header(self):
        return self.driver.find_element(By.XPATH, self.__header_text).text

    def enter_firstname(self, value):
        firstname = self.driver.find_element(By.NAME, self.__firstname_textBox)
        firstname.send_keys(value)
        firstname.clear()
    def enter_lastname(self, value):
        lastname = self.driver.find_element(By.NAME, self.__secondname_textBox)
        lastname.send_keys(value)
        lastname.clear()

    def get_first_name_error_message(self, value):
       base_utils.find_element(self.driver,  self.__first_name_error_message_icon, "first name error message icon").click()
        #return base_utils.wait_for_element(self.driver, (By.XPATH, self.__firstname_error_message), value).text

    def get_surname_error_message(self, value):
        base_utils.find_element(self.driver, self.__surname_error_message_icon, "surname error message icon").click()
        #time.sleep(120)
        #return base_utils.wait_for_element(self.driver, (By.XPATH, self.__surname_error_message), value).text