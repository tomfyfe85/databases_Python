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
        User(4, "viv", "viv@viv.com"),
    ]


"""
When we call UserRepository#delete
We remove a record from the database.
"""


def test_delete_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User(None, "viv", "viv@viv.com")
    assert repository.create(user) == None

    assert repository.delete(1) == None

    users = repository.all()

    assert users == [
        User(2, "chants", "chants@twtw.com"),
        User(3, "kipper", "kipper@steak.com"),
        User(4, "viv", "viv@viv.com"),
    ]


def test_update_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    user.email = "BIGcHANTZ@twtw.com"
    assert repository.update(user) == None
    assert repository.all() == [
        User(1, "tom", "fyfe@keg.com"),
        User(2, "chants", "BIGcHANTZ@twtw.com"),
        User(3, "kipper", "kipper@steak.com")]