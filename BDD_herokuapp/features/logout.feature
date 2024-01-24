Feature: Test the secure page on the-internet.herokuapp.com webpage

  Background:
    Given Home page: I am on the-internet.herokuapp.com

  @Secure
  Scenario Outline:
    When Home page: I look for "<element>" and I click on it
    When Login page: I enter "<username>" in the username text field
    When Login page: I enter "<password>" in the password text field
    When Login page: I click on login button
    When Secure page: I read the "You logged into a secure area!" message
    When Secure page: I click on logout button
    Then Login page: I read the "You logged out of the secure area!" message
    Examples:
      | element             | username | password             |
      | Form Authentication | tomsmith | SuperSecretPassword! |
