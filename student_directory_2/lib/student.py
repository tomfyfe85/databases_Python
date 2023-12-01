class Student:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, student_name, cohort_id):
        self.id = id
        self.student_name = student_name
        self.cohort_id = cohort_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Student({self.id}, {self.student_name}, {self.cohort_id})"
