from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
import datetime

date1 = datetime.date(2023, 6, 1)
date2 = datetime.date(2023, 7, 4)
date3 = datetime.date(2023, 9, 3)

"""
When we call CohortRepository#all
We get a list of Cohort objects reflecting the seed data.
"""


def test_get_all_cohorts(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed(
        "seeds/student_directory_2.sql"
    )  # Seed our database with some test data
    repository = CohortRepository(db_connection)  # Create a new CohortRepository

    cohorts = repository.all()  # Get all cohorts

    # Assert on the results
    assert cohorts == [
        Cohort(1, "June 22", date1),
        Cohort(2, "July 22", date2),
        Cohort(3, "August 22", date3),
    ]


"""
When we call CohortRepository#find
We get a single Cohort object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    artist = repository.find(3)
    assert artist == Cohort(3, "August 22", date3)


"""
# When I call #find_with_students with a cohort id
# I get a the cohort with a list of it's students, prepopulated 
# """

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, "June 22", date1, [
        Student(1, 'Tom', 1),
        Student(3, 'Viv', 1),
    ])
        
    

"""
When we call CohortRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    date4 = datetime.date(2023, 10, 7)
    repository.create(Cohort(None, "Oct 22", date4))

    result = repository.all()
    assert result == [
        Cohort(1, "June 22", date1),
        Cohort(2, "July 22", date2),
        Cohort(3, "August 22", date3),
        Cohort(4, "Oct 22", date4),
    ]


"""
When we call CohortRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Cohort(1, "June 22", date1),
        Cohort(2, "July 22", date2),
    ]

