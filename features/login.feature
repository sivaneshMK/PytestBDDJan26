Feature: Login Functionality

  @signup
  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username and password
    And clicks on login button
    Then user should be redirected to the dash board
