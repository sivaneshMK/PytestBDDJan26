import allure
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

from pages.login_page import LoginPage

scenarios("..//features/login.feature")

# @pytest.fixture
# def login_page(driver):
#     return LoginPage(driver)

@pytest.fixture()
@given("user is on the login page")
def launch_app(driver):
    return LoginPage(driver)

@when("user enters valid username and password")
def enter_credentials(launch_app):
    launch_app.enter_user_credentials("username", "password")

@when("clicks on login button")
def click_on_login_button(launch_app):
    launch_app.click_on_login_button()

@then("user should be redirected to the dash board")
def verify_user_loggedin(driver):
    title = driver.title
    # allure.attach(driver.get_screenshot_as_png(),
    #               name="Home Page",
    #               attachment_type=allure.attachment_type.PNG)
    assert title =="home", "user is not land on home page"

@when(parsers.cfparse('user enters invalid username "{username}" and password "{password}"'))
def enter_invalid_info(launch_app, username, password):
    launch_app.enter_user_credentials(username, password)

@when(parsers.cfparse("enter valid username {username}"))
def enter_username(launch_app, username):
    launch_app.enter_username(username)


@when(parsers.cfparse("enter invalid password {password}"))
def enter_username(launch_app, password):
    launch_app.enter_password(password)