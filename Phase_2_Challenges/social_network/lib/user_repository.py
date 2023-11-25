from lib.user import User


class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from users")
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"])
            users.append(item)
        return users

    # Find a single artist by their id
    def find(self, user_id):
        rows = self._connection.execute("SELECT * from users WHERE id = %s", [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)", [user.name, user.email]
        )
        return None

    # # Delete an artist by their id
    # def delete(self, artist_id):
    #     self._connection.execute(
    #         'DELETE FROM artists WHERE id = %s', [artist_id])
    #     return None
