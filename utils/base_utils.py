import allure
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(driver, element, value):
    wait = WebDriverWait(driver, timeout=10)
    return wait.until(EC.text_to_be_present_in_element(element, value))

def find_element(driver, locator, field_name):
    try:
        return driver.find_element(By.XPATH, locator)
    except NoSuchElementException:
        allure.attach(f"failed to find the {field_name}")
        pytest.fail(f"Failed to identify the {field_name}")