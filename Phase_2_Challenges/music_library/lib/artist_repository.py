from lib.artist import Artist


class ArtistRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute("SELECT * from artists")
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    def find(self, artist_id):
        rows = self._connection.execute(
            "SELECT * from artists WHERE id = %s", [artist_id]
        )
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    def find_with_albums(self, artist_id):
        rows = self._connection.execute(
            "SELECT * FROM artists JOIN albums ON artists.id = albums.artist_id"
            "WHERE artist_id =  %s"[artist_id]
        )
        # 11.45 in on the vid. method unfinished

    # # Create a new artist
    # # Do you want to get its id back? Look into RETURNING id;``
    def create(self, artist):
        self._connection.execute(
            "INSERT INTO artists (name, genre) VALUES (%s, %s)",
            [artist.name, artist.genre],
        )
        return None

    def delete(self, artist_id):
        self._connection.execute("DELETE FROM artists WHERE id = %s", [artist_id])
        return None
