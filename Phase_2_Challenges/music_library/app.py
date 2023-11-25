from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# connection = DatabaseConnection()
# connection.connect()
# connection.seed("seeds/music_library.sql")
class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager! \n")
        print(
            "What would you like to do? \n1 - List all albums \n2 - List all artists \n"
        )
        library_choice = input("Enter your choice:")
        if library_choice == "2":
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            print("\nHere is the list of artists:")
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        elif library_choice == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            print("\nHere is the list of albums:")
            for album in albums:
                print(
                    f"{album.id}: {album.title} ({album.release_year}) ({album.artist_id})"
                )


if __name__ == "__main__":
    app = Application()
    app.run()


# # if __name__ == "__main__":
#     app = Application()
#     app.run()
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
