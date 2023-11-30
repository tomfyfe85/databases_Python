class User:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    # # This method allows our tests to assert that the objects it expects
    # # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email})"
