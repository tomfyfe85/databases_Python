from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects recflecting the seed data.
"""


def test_get_all_posts(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed(
        "seeds/social_network.sql"
    )  # Seed our database with some test data
    repository = PostRepository(db_connection) 

    posts = repository.all()

    assert posts == [
        Post(1, "new album!", "PYRAMID POWER BABY!", 666, 1),
        Post(2, "new live show", "we are on this week", 100, 2),
        Post(3, "el beers", "tour beers are good beers", 110000, 3),
    ]


"""
When we call PostRepository#find
We get a single Artist object reflecting the seed data.
"""


def test_get_single_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == Post(2, "new live show", "we are on this week", 100, 2)


"""
When we call PostRepository#create
We get a new record in the database.
"""


def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = Post(None, "new Title", "new Content", 9, 2)
    assert repository.create(post) == None

    posts = repository.all()

    assert posts == [
        Post(1, "new album!", "PYRAMID POWER BABY!", 666, 1),
        Post(2, "new live show", "we are on this week", 100, 2),
        Post(3, "el beers", "tour beers are good beers", 110000, 3),
        Post(4, "new Title", "new Content", 9, 2),
    ]


# """
# When we call PostRepository#delete
# We remove a record from the database.
# """


# def test_delete_post(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = PostRepository(db_connection)
#     post = Post(4, "new post", "new content", 9, 2)
#     assert repository.create(post) == None

#     assert repository.delete(1) == None

#     posts = repository.all()

#     assert posts == [
#         Post(2, "chants", "chants@twtw.com"),
#         Post(3, "kipper", "kipper@steak.com"),
#         Post(4, "viv", "viv@viv.com"),
#     ]
