Feature: Testing if 'SIGN-UP' area working properly

  Background:
    Given sign in: I am a user on jules sign in page

    @sign_up
    Scenario: Check if user can create an account using 'PERSONAL' option

      When sign_up: I click sign up button
      When sign_up: I click personal button
      When sign_up: I click CONTINUE button
      When sign_up: I type my first name  "Popa"
      When sign_up: I click CONTINUE button
      When sign_up: I type my last name  "Georgian-Victor"
      When sign_up:I click CONTINUE button
      When sign_up: I set my email to "test"
      Then sign_up: I receive message:Please enter a valid email address
      When sign_up: I set my email to "popa.georgian93@gmail.com"
      When sign_up: I click CONTINUE button
      When sign_up: I complete Password field which respects the security conditions
      When sign_up: I click CONTINUE button
      When sign_up: I enter an different password
      Then sign_up: I receive message:passwords do not match
      When sign_up: I Confirm your password... with right password
      When sign_up: I click SIGN_UP button
      When sign_up: I click on VERIFY YOUR EMAIL button from my email inbox
      When sign_up: Site is opened and I got the message 'Activation Successfully'




