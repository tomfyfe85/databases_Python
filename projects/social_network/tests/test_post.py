from lib.post import Post

"""
Post constructs with an id, contents, number of views and user id
"""


def test_post_constructs():
    post = Post(1, "Test Title", "Test Content", "Test Number_of_Views", "Test User_id")
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.content == "Test Content"
    assert post.number_of_views == "Test Number_of_Views"
    assert post.user_id == "Test User_id"


"""
We can format artists to strings nicely
"""


def test_posts_format_nicely():
    post = Post(1, "Test Title", "Test Content", "Test Number_of_Views", "Test User_id")
    assert str(post) == "Post(1, Test Title, Test Content, Test Number_of_Views, Test User_id)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.


"""
We can compare two identical artists
And have them be equal
"""


def test_posts_are_equal():
    post1 = Post(1, "Test Title", "Test Content", "Test Number_of_Views", "Test User_id")
    post2 = Post(1, "Test Title", "Test Content", "Test Number_of_Views", "Test User_id")
    assert post1 == post2
# Try commenting out the `__eq__` method in lib/post.py
# And see what happens when you run this test again.
