Feature: Books can be stored

    Scenario: create a book
        Given we create a new book
        Then pages is initially set to 0

    Scenario: title and author are saved for books
        Given we create a new book
        Then we have an author set
        And we have a title set

    Scenario: we can print the books title
        Given we have a book created
        When we print the books information
        Then we should see the books title

    Scenario: we can print the books author
        Given we have a book created
        When we print the books information
        Then we should see the books author

    Scenario: we can print the number of pages
        Given we have a book created
        When we print the books information
        Then we should see the number of pages
