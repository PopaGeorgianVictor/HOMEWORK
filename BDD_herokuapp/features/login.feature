Feature: Test the login functionality on the-internet.herokuapp.com webpage

  Background:
    Given Home page: I am on the-internet.herokuapp.com

    @Login
  Scenario:
    When Home page: I look for "Form Authentication" and I click on it
    When Login page: I enter "tomsmith" in the username text field
    When Login page: I enter "SuperSecretPassword!" in the password text field
    When Login page: I click on login button
    Then I am on the secured area
