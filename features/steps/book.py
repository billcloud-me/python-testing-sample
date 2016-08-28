from behave import *
from Books.Book import Book
from mock import mock, MagicMock
from io import StringIO

@given('we create a new book')
def step_impl(context):
    context.test_title = test_title = "title"
    context.test_author = test_author = "author"
    book = Book(test_title, test_author)
    context.test_book = book

@given('we have a book created')
def step_impl(context):
    context.test_title = test_title = "title"
    context.test_author = test_author = "author"
    book = Book(test_title, test_author)
    context.test_book = book
    context.test_pages = test_pages = 200
    context.test_book.setPages(test_pages)

@when('we print the books information')
def step_impl(context):
    with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
        print(context.test_book)
    context.fake_stdout = fake_stdout

@then('pages is initially set to 0')
def step_impl(context):
    assert context.test_book.pages == 0

@then('we have an author set')
def step_impl(context):
    assert context.test_book.author == context.test_author

@then('we have a title set')
def step_impl(context):
    assert context.test_book.title == context.test_title

@then('we should see the books title')
def step_impl(context):
    assert "Title: " + context.test_title in context.fake_stdout.getvalue()

@then('we should see the books author')
def step_impl(context):
    assert "Author: " + context.test_author in context.fake_stdout.getvalue()

@then('we should see the number of pages')
def step_impl(context):
    assert "Pages: " + str(context.test_pages) in context.fake_stdout.getvalue()
