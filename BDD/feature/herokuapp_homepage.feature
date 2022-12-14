
Feature: Testing access to the pages: '/login', '/secure' of herokuapp

  Scenario: Check that the user can access pages of herokuapp
    Given Home page: I am on herokuapp homepage
    When Home page: I click on Form Authentication
