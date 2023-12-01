from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""


def test_get_all_records(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blog.sql")  # Seed our database with some test data
    repository = PostRepository(db_connection)  # Create a new PostRepository

    posts = repository.all()  # Get all artists

    # Assert on the results
    assert posts == [
        Post(1, "post1", "content1"),
        Post(2, "post2", "content2"),
        Post(3, "post3", "content3"),
        Post(4, "post4", "content4"),
    ]


# """
# When we call ArtistRepository#find
# We get a single Artist object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)

#     artist = repository.find(3)
#     assert artist == Artist(3, "Taylor Swift", "Pop")

# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)

#     repository.create(Artist(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(3, "Taylor Swift", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#         Artist(5, "The Beatles", "Rock"),
#     ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#     ]
