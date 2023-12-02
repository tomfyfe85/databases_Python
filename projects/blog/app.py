from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog.sql")

# Retrieve all artists
post_repository = PostRepository(connection)
post = post_repository.find_with_comments(3)

print(post)
