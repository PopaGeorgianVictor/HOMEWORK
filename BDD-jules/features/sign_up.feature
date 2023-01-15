Feature: Testing if 'SIGN-UP' area working properly

  Background:
    Given sign in: I am a user on jules sign in page

    @jules_test_debug
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
      When sign_up: I set my email to "test@mail.com"
      When sign_up:I click CONTINUE button