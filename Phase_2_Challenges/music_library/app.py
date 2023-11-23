from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
for artist in artist_repository.all():
    print(artist)

# Find an artist
print(artist_repository.find(2))

# Retrieve all albums
album_repository = AlbumRepository(connection)
for album in album_repository.all():
    print(album)


