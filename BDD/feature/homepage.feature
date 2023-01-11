Feature: Testing access to '/login' page of herokuapp

  @homepage
  Scenario: Check that the user can access '/login' page of herokuapp
    Given : I am on herokuapp homepage
    When : I click on Form Authentication
    Then : I am able to enter on page


