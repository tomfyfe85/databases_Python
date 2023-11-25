from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository

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
for user in users:
    print(user)

# find specific user
user2 = user_repository.find(2)
print(f"{user2} is user 2")
