from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# # Seed with some seed data
connection.seed("seeds/blog.sql")

# # Retrieve all artists
post_repository = PostRepository(connection)
post_comments = post_repository.find_with_comments(3)
# post_all = post_repository.al()
# print("hello")
# print(post_repository.find(2))
# print(post_comments.comments)

for post in [post_comments]:
    print()
    print("post")
    print(post)
    print()
    print("comments")
    for comment in post.comments:
        print(comment)
