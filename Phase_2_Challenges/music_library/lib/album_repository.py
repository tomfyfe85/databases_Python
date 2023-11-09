from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        result = self.connection.execute("SELECT * FROM albums")
        # Executes the SQL query:
        # SELECT title, release_year, artist_id FROM albums
        albums = []
        for row in result:
            album = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums