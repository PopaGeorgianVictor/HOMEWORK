Feature: Test the homepage on the-internet.herokuapp.com webpage

  Background:
    Given Home page: I am on the-internet.herokuapp.com

    @Home
  Scenario Outline: Check that the homepage has access to different elements
    When Home page: I look for "<element>" and I click on it
    Then I am on the "<element_page>" page
    Examples:
      | element               | element_page                                                     |
      | Form Authentication   | https://the-internet.herokuapp.com/login                         |
      | Forgot Password       | https://the-internet.herokuapp.com/forgot_password               |
      | Notification Messages | https://the-internet.herokuapp.com/notification_message_rendered |
