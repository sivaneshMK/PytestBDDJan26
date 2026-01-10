import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    yield driver
    driver.quit()
