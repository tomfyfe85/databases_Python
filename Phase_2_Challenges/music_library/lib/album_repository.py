from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        result = self._connection.execute("SELECT * FROM albums")

        return [
            Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            for row in result
        ]

    def find(self, album_id):
        rows = self._connection.execute("SELECT * from albums WHERE id = %s", [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
