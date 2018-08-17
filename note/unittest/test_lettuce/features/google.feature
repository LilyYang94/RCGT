Feature: Go to google
  Scenario: Visit Google
    Given I go to "http://www.baidu.com/"
    When I fill in field with class "gsfi" with "selenium"
    Then I should see "seleniumhq.org" within 2 second
