Feature: Testing logout buton and if info message is displayed on '/login' page after I logout

  @logout
  Scenario: Check that the user can access '/secure' page of herokuapp
    Given : I am on '/secure' page
    When : I clicked on Logout button
    Then : I successfully logout and redirect to the '/login' page and info message ' You logged out of the secure area!' is displayed in a green tab