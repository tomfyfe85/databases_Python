from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""


def test_get_all_records(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed(
        "seeds/music_library.sql"
    )  # Seed our database with some test data
    repository = ArtistRepository(db_connection)

    artists = repository.all()  # Get all artists

    # Assert on the results
    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]


"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3)
    assert artist == Artist(3, "Taylor Swift", "Pop")


def test_create_records(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed(
        "seeds/music_library.sql"
    )  # Seed our database with some test data
    repository = ArtistRepository(db_connection)

    artist = Artist(None, "The Beatles", "Rock")
    assert repository.create(artist) == None

    results = repository.all()
    assert results == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "The Beatles", "Rock"),
    ]


"""
When we call ArtistRepository#delete
We remove a record from the database.
"""


def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    assert repository.delete(3) == None

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]


"""
When I call #find_with_albums with an artist is 
Then I get the artist with a list of their albums, prepopulated.
"""


def test_find_with_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find_with_albums(1)
    assert artist == Artist(
        1,
        "Pixies",
        "Rock",
        [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1),
            Album(5, "Bossanova", 1990, 1),
        ],
    )
