class Post:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, content, number_of_views, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.number_of_views = number_of_views
        self.user_id = user_id

    # # This method allows our tests to assert that the objects it expects
    # # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.number_of_views}, {self.user_id})"
