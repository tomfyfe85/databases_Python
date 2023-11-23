from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection 

    # Selecting all records
    # No arguments
    def all(self):
        result = self.connection.execute("SELECT * FROM albums")
        print(result)

        return [Album(row['id'], row["title"], row["release_year"], row["artist_id"])
                for row in result]