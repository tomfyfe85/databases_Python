class Album:
    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Artists({self.id}, {self.name}, {self.genre})"
