from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""


def test_get_all_users(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed(
        "seeds/social_network.sql"
    )  # Seed our database with some test data
    repository = UserRepository(db_connection)  # Create a new ArtistRepository

    users = repository.all()

    assert users == [
        User(1, "tom", "fyfe@keg.com"),
        User(2, "chants", "chants@twtw.com"),
        User(3, "kipper", "kipper@steak.com"),
    ]


"""
When we call UserRepository#find
We get a single Artist object reflecting the seed data.
"""


def test_get_single_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, "chants", "chants@twtw.com")


"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    
    user = User(None, "viv", "viv@viv.com")
    assert repository.create(user) == None

    users = repository.all()

    assert users == [
        User(1, "tom", "fyfe@keg.com"),
        User(2, "chants", "chants@twtw.com"),
        User(3, "kipper", "kipper@steak.com"),
        User(4, "viv", "viv@viv.com")
    ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = ArtistRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#     ]
