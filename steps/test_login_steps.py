import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

from pages.login_page import LoginPage

scenarios("..//features/login.feature")

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@given("user is on the login page")
def launch_app(login_page):
    pass

@when("user enters valid username and password")
def enter_credentials(login_page):
    login_page.enter_user_credentials("username", "password")

@when("clicks on login button")
def click_on_login_button(login_page):

    login_page.click_on_login_button()

@then("user should be redirected to the dash board")
def verify_user_loggedin(login_page):
    title = login_page.title
