Feature: Search Bukalapak

    Scenario: Search Bukalapak with keywords
        Given I am on the Bukalapak page
        When I search for "<keywords>"
        Then the page title should have "<keywords>"

        Examples:
            | keywords  |
            | Macbook   |
            | Handphone |