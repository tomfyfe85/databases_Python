from lib.cohort import Cohort


class CohortRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all cohorts
    def all(self):
        rows = self._connection.execute("SELECT * from cohorts")
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        print(type(cohorts[0].starting_date))
        return cohorts

    # Find a single artist by their id
    def find(self, cohort_id):
        rows = self._connection.execute(
            "SELECT * from cohorts WHERE id = %s", [cohort_id]
        )
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])

    # # Create a new artist
    # # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute('INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)', [
                                artist.name, artist.starting_date])
        return None

    # # Delete an artist by their id
    def delete(self, student_id):
        self._connection.execute(
            'DELETE FROM cohorts WHERE id = %s', [student_id])
        return None
