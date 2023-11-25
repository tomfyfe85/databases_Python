from lib.post import Post


class PostRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from posts")
        posts = []
        for row in rows:
            item = Post(
                row["id"], row['title'], row["content"], row["number_of_views"], row["user_id"]
            )
            posts.append(item)
        return posts

    # Find a single user by their id
    def find(self, post_id):
        rows = self._connection.execute("SELECT * from posts WHERE id = %s", [post_id])
        row = rows[0]
        return  Post(row["id"], row['title'], row["content"], row["number_of_views"], row['user_id'])

    # Create a new user
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, post):
        self._connection.execute(
            "INSERT INTO posts (title, content, number_of_views, user_id) VALUES (%s, %s, %s, %s)", [post.title, post.content, post.number_of_views, post.user_id]
        )
        return None

    # # Delete an user by their id
    def delete(self, post_id):
        self._connection.execute("DELETE FROM posts WHERE id = %s", [post_id])
        return None
