import pytest
from pytest_bdd import given, parsers, when, scenarios

from pages.login_page import LoginPage
from pages.signup_page import SignupPage

scenarios("..//features/signup.feature")

@pytest.fixture()
@given("user is on the login page")
def launch_app(driver):
    return LoginPage(driver)

@when(parsers.cfparse("navigated to the signup page"))
def click_on_create_newaccount(launch_app):
    launch_app.click_on_create_new_account_button()

@pytest.fixture()
def signup(driver):
    return SignupPage(driver)

@when(parsers.cfparse("user enters details"))
def enter_user_details(datatable, signup):
    #data = {row["field"]: row["value"] for row in datatable}
    print(datatable)
    for data in datatable:
        signup.enter_firstname(data[0])
        firestname_error = signup.get_first_name_error_message("What's your name?")
        #assert firestname_error =="What's your name?", "The firstname Error message is not getting matched"
        signup.enter_lastname(datatable[1])
        surname_error = signup.get_surname_error_message("What's your name?")
        #3assert surname_error == "What's your name?", "The surname Error message is not getting matched"






