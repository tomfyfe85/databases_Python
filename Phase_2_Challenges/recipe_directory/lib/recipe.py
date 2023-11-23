class Recipe:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, cooking_time, rating_1_to_5):
        self.id = id
        self.name = name
        self.cooking_time = cooking_time
        self.rating_1_to_5 = rating_1_to_5

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Recipe({self.id}, {self.name}, {self.cooking_time}, {self.rating_1_to_5})"
