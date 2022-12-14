
Feature: Testing access to the pages: '/login', '/secure' of herokuapp

  Scenario: Check that the user can access '/login' page of herokuapp
    Given Home page: I am on herokuapp homepage
    When Home page: I click on Form Authentication
    Then : I am able to enter on page

   Scenario: Check that the user can access '/secure' page of herokuapp
    Given Home page: I am on herokuapp homepage
    When Home page: I click on Form Authentication
    When : I enter correct username and password
    When : I clicked on Login button
    Then : I successfully enter on '/secure' page

  Scenario: Check that the user can logout of the '/secure' page
    Given Secure Page: I am on '/secure' page
    When Secure Page: I click on Logout button
    Then : I successfully logout and redirect to the '/login' page

   Scenario: Check if the info message 'You logged into a secure area!' appears  on '/secure' page
    Given Secure Page: I am on '/secure' page
    When Secure Page: I click on Logout button
    Then : I successfully logout and redirect to the '/login' page