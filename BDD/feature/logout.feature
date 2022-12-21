Feature: Testing logout buton and if info message is displayed on '/login' page after I logout


  Scenario: Check that the user can access '/secure' page of herokuapp
    Given : I am on '/secure' page
    When : I enter correct username and password
    When : I clicked on Login button
    Then : I successfully enter on '/secure' page and info message 'You logged into a secure area!' is displayed in a green tab