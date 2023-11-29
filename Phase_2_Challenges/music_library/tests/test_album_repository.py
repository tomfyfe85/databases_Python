from lib.album import Album
from lib.album_repository import AlbumRepository


"""
When I call #all on the AlbumRepository
I get all the albums back in a list
"""


def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    result = repo.all()
    assert result == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
    ]

"""
When I call #find on the AlbumRepository 
I can get a specific Album object back, given I enter
the correct the album_id
"""

def test_finds_a_specific_album_by_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(2)
    assert album == Album(2, "Surfer Rosa", 1988, 1)

"""

"""

def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = Album(None, "test", 2000, 1)
    assert repository.create(album) == None

    result = repository.all()
    assert result == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "test", 2000, 1)
    ]


# """
# When we call PostRepository#delete
# We remove a record from the database.
# """


# def test_delete_post(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = PostRepository(db_connection)
#     post = Post(4, "new Title", "new Content", 9, 2)
#     assert repository.create(post) == None

#     assert repository.delete(1) == None

#     posts = repository.all()

#     assert posts == [
#         Post(2, "new live show", "we are on this week", 100, 2),
#         Post(3, "el beers", "tour beers are good beers", 110000, 3),
#         Post(4, "new Title", "new Content", 9, 2),
#     ]
