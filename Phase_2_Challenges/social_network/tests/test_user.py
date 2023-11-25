from lib.user import User

"""
User constructs with an id, name and email
"""
def test_user_constructs():
    user = User(1, "Test User", "Test Email")
    assert user.id == 1
    assert user.name == "Test User"
    assert user.email == "Test Email"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    user = User(1, "Test User", "Test Email")
    assert str(user) == "User(1, Test User, Test Email)"
    # Try commenting out the `__repr__` method in lib/user.py
    # And see what happens when you run this test again.

# """
# We can compare two identical artists
# And have them be equal
# """
# def test_artists_are_equal():
#     user1 = User(1, "Test User", "Test Email")
#     user2 = User(1, "Test Artist", "Test Email")
    # assert user1 == user2
    # Try commenting out the `__eq__` method in lib/user.py
    # And see what happens when you run this test again.
