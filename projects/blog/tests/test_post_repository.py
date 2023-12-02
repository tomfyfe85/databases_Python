from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

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


"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, "post3", "content3")


"""
When I call #find_with_comments with a comment id 
Then I get the post with a list of its comments, prepopulated.
"""


def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)

    post = repository.find_with_comments(3)
    assert post == Post(
        3,
        "post3",
        "content3",
        [Comment(3, "yo", "author3", 3), Comment(4, "siiccck", "author4", 3)],
    )


"""
When we call PostRepository#create
We get a new record in the database.
"""


def test_create_record(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, "post5", "content5"))

    posts = repository.all()
    assert posts == [
        Post(1, "post1", "content1"),
        Post(2, "post2", "content2"),
        Post(3, "post3", "content3"),
        Post(4, "post4", "content4"),
        Post(5, "post5", "content5"),
    ]


"""
When we call ArtistRepository#delete
We remove a record from the database.
"""


def test_delete_record(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)  # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Post(1, "post1", "content1"),
        Post(2, "post2", "content2"),
        Post(4, "post4", "content4"),
    ]
