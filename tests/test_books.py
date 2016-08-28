from Books.Book import Book
import pytest
from mock import mock, MagicMock

class TestBooks:
    
    def setupBook(self):
        book = Book("test", "test")
        book.setPages(200)
        return book

    def test_init(self):
        book = Book("test", "test")
        assert hasattr(book, "author")
        assert hasattr(book, "title")
        assert hasattr(book, "pages")
        assert book.pages == 0

    def test_set_pages(self):
        book = self.setupBook()
        assert book.pages == 200

    def test_to_str(self):
        book = self.setupBook()
        with mock.patch('sys.stdout') as fake_stdout:
            print(book)
        fake_stdout.assert_has_calls([
            mock.call.write('Author: test\nTitle: test\nPages: 200\n'),
            ])
