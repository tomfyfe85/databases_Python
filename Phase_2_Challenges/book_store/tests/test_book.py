from lib.book import Book

"""
Book constructs with an id, name and genre
"""


def test_book_constructs():
    book = Book(1, "test book", "test author")
    assert book.id == 1
    assert book.title == "test book"
    assert book.author_name == "test author"
