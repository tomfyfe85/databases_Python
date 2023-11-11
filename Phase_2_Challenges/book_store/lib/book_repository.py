from lib.book import Book


class BookRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from books")
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
