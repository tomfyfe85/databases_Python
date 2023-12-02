# from lib.post import Comment

# """
# Post constructs with an id, name and genre
# """
# def test_Post_constructs():
#     post = Post(1, "Test Post", "Test Genre")
#     assert post.id == 1
#     assert post.title == "Test Post"
#     assert post.post_content == "Test Genre"

# """
# We can format posts to strings nicely
# """
# def test_artists_format_nicely():
#     post = Post(1, "Test title", "Test content")
#     assert str(post) == "Post(1, Test title, Test content)"
#     # Try commenting out the `__repr__` method in lib/post.py
#     # And see what happens when you run this test again.

# """
# We can compare two identical posts
# And have them be equal
# """
# def test_artists_are_equal():
#     post1 = Post(1, "Test post", "Test content")
#     post2 = Post(1, "Test post", "Test content")
#     assert post1 == post2
#     # Try commenting out the `__eq__` method in lib/artist.py
#     # And see what happens when you run this test again.
