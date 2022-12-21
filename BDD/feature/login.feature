Feature: Testing access to '/secure' page of herokuapp

  Scenario: Check that the user can access '/secure' page of herokuapp
    Given : I am on '/secure' page
    When : I enter correct username and password
    When : I clicked on Login button
    Then : I successfully enter on '/secure' page