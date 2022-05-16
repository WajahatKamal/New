Feature: To Verify the Login process
  As a QA I want to verify the Login for CrossFund web platform

  Background:
    Given User Setups the Web Browser
    When User Navigates to "https://develop.crossfund.app/" Url
    Then User clicks on Login button
#    And User lands on the login page


  Scenario: Verify User is successfully logged in

    Given User is on the login page
    When User Enters "valid.username" on UserName Field on Login Page
    Then User Enters "valid.password" on Password Field on Login Page
    And User Clicks on Login Button on Login Page
    And User Successfully Logs in to CrossFund platform

  Scenario: Verify Internal Invitation sent successfully

    Given User is on the login page
    When User Enters "valid.username" on UserName Field on Login Page
    Then User Enters "valid.password" on Password Field on Login Page
    And User Clicks on Login Button on Login Page
    And User Successfully Logs in to CrossFund platform
    And User clicks on the Profile button
    And User clicks on Invitation from the left menu
    And User Enters the First Name
    And User Enters the Last Name
    And User Enters the Email Address
    And User Selects the Campaign from the dropdown Menu
    And User clicks on Send button
