from lib.user import User


class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from users ORDER BY id ASC")
        return [User(row["id"], row["name"], row["email"]) for row in rows]

    # Find a single user by their id
    def find(self, user_id):
        rows = self._connection.execute("SELECT * from users WHERE id = %s", [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"])

    # Create a new user
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)", [user.name, user.email]
        )
        return None

    # Delete an user by their id
    def delete(self, user_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None

    def update(self, user):
        self._connection.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            [user.name, user.email, user.id],
        )
