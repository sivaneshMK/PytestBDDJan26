Feature: Signup Functionality

  Background:
    Given user is on the login page

    @signup
    Scenario: Field Validation for Signup Page
      When navigated to the signup page
      And user enters details
      |  abcdXYz  |  usisksls|
      |  123344333| 8893893983|

