class Comment:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, comment_content, author, post_id):
        self.id = id
        self.comment_content = comment_content
        self.author = author
        self.post_id = post_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return (
            f"Comment({self.id}, {self.comment_content}, {self.author}, {self.post_id})"
        )
