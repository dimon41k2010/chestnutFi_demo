Feature: Navbar

  Scenario: Navbar is displayed
    Given User on the homepage
    Then User should see the navbar

  Scenario: Navbar contains links
    Given User on the homepage
    Then User should see a link to "Home"
    And User should see a link to "About"
    And User should see a link to "Contact"

  Scenario: Navbar links are functional
    Given User on the homepage
    When User clicks on the "About" link
    Then User should be redirected to the About page
    When User clicks on the "Contact" link
    Then User should be redirected to the Contact page