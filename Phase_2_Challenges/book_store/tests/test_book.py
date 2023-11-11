from lib.book import Book

"""
Book constructs with an id, name and genre
"""


def test_book_constructs():
    book = Book(1, "test title", "test author")
    assert book.id == 1
    assert book.title == "test title"
    assert book.author_name == "test author"

def test_books_format_nicely():
    book = Book(1, 'test title', 'test author')
    assert str(book) == "Book(1, test title, test author)"