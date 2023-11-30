from lib.book_repository import BookRepository
from lib.book import Book

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""


def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    books = BookRepository(db_connection)

    assert books.all() == [
        Book(1, "Nineteen Eighty-Four", "George Orwell"),
        Book(2, "Mrs Dalloway", "Virginia Woolf"),
        Book(3, "Emma", "Jane Austen"),
        Book(4, "Dracula", "Bram Stoker"),
        Book(5, "The Age of Innocence", "Edith Wharton"),
    ]
