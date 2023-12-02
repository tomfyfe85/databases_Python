from lib.post import Post
from lib.comment import Comment


class PostRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute("SELECT * from posts")
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["post_content"])
            posts.append(item)
        return posts

    # Find a single artist by their id
    def find(self, post_id):
        rows = self._connection.execute("SELECT * from posts WHERE id = %s", [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["post_content"])

    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            "SELECT * FROM posts JOIN comments ON posts.id = comments.post_id \
                WHERE post_id = %s",
            [post_id],
        )
        comments = []
        for row in rows:
            comment = Comment(
                row["id"], row["comment_content"], row["author"], row["post_id"]
            )
            comments.append(comment)
        # print(comments)
        post = Post(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)
        return post

    # The comments dictionary is being populated but not appearing 
    # in the new instance of post 



    # Create a new post
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, post):
        self._connection.execute(
            "INSERT INTO posts(title, post_content) VALUES (%s, %s)",
            [post.title, post.post_content],
        )
        return None

    # # Delete an artist by their id
    def delete(self, post_id):
        self._connection.execute("DELETE FROM posts WHERE id = %s", [post_id])
        return None
