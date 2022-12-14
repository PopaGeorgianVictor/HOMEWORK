Feature: Testing access to '/secure' page of herokuapp and if info message is displayed on this pages

  @login
  Scenario: Check that the user can access '/secure' page of herokuapp
    Given : I am on '/login' page
    When : I enter correct username and password
    When : I clicked on Login button
    Then : I successfully enter on '/secure' page and info message 'You logged into a secure area!' is displayed in a green tab