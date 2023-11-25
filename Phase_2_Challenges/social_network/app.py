from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User

# from lib.post_repository import PostRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all users
user_repository = UserRepository(connection)
users = user_repository.all()
# List them out
print('\n')
print("ALL USERS")
for user in users:
    print(user)
print("\n")
# find specific user
print("USER FOUND")
user2 = user_repository.find(2)
print(f"{user2} is user 2 \n")

# create add new user to the database
user = User(None, "NEW USER", "new@email.com")
user_repository.create(user)
newUser = user_repository.all()
print("NEW USER ADDED")
for users in newUser:
    print(users)
