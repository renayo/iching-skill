Feature: random-hexagram
  Scenario: Request a random hexagram
    Given an english speaking user
     When the user says "iching"
     Then "iching" should reply with dialog from "iching.dialog"
