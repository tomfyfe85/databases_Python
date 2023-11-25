from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")


if __name__ == "__main__":
    app = Application()
    app.run()
# Retrieve all artists
# artist_repository = ArtistRepository(connection)
# for artist in artist_repository.all():
#     print(artist)

# Find an artist
# print(artist_repository.find(2))

# Retrieve all albums
# album_repository = AlbumRepository(connection)
# for album in album_repository.all():
#     print(album)
