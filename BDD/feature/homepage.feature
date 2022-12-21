Feature: Testing access to '/login' page

  Scenario: Check that the user can access '/login' page of herokuapp
    Given : I am on herokuapp homepage
    When : I click on Form Authentication
    Then : I am able to enter on page

   Scenario: Check that the user can access '/secure' page of herokuapp
    Given : I am on herokuapp homepage
    When : I click on Form Authentication
    When : I enter correct username and password
    When : I clicked on Login button
    Then : I successfully enter on '/secure' page

  Scenario: Check that the user can logout of the '/secure' page
    Given : I am on '/secure' page
    When : I click on Logout button
    Then : I successfully logout and redirect to the '/login' page

   Scenario: Check if the info message 'You logged into a secure area!' appears  on '/secure' page
    Given : I am on '/login' page
    When : I enter correct username and password
    When : I click on Logout button
    Then : I enter on '/secure' page and info message 'You logged into a secure area!' is displayed in a green tab

  Scenario: Check if the info message ' You logged out of the secure area! ' appears  on '/login' page after I logout on the '/secure' page
    Given : I am on '/secure' page
    When : I click on Logout button
    Then : I successfully logout and redirect to the '/login' page and info message ' You logged out of the secure area!' is displayed in a green tab