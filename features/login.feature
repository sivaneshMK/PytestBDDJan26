Feature: Login Functionality

  @signin
  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username and password
    And clicks on login button
    Then user should be redirected to the dash board

  @signin @signin_negative
  Scenario: Unsuccessful login with invalid credentials
    Given user is on the login page
    When user enters invalid username "sivanesh" and password "abcd@123"
    And clicks on login button

  @signin_field_validation @signin
  Scenario Outline: Login with multiple users
    Given user is on the login page
    When user enters invalid username "<username>" and password "<password>"
    And clicks on login button

    Examples:
      | username  | password     |
      |  sivanesh | password@123 |
      |  admin    | Admin@123    |

  @wip
  Scenario: Invalid Login using But
    Given user is on the login page
    When enter valid username "abcdefghijk"
    But enter invalid password "abcd@1223"
    And clicks on login button
    Then user should be redirected to the dash board
