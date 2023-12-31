from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")

# Retrieve all Cohorts
cohort_repository = CohortRepository(connection)
cohort = cohort_repository.find_with_students(1)

# List them out
for cohort in [cohort]:
    print()
    print("cohort")
    print(cohort) 
    print()
    
    print("students")
    for student in cohort.students:
        print(student)
print()