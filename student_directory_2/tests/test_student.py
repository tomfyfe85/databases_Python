from lib.student import Student

"""
student constructs with an id, student_name and genre
"""


def test_student_constructs():
    student = Student(1, "Test student", 1)
    assert student.id == 1
    assert student.student_name == "Test student"
    assert student.cohort_id == 1


"""
We can format students to strings nicely
"""


def test_students_format_nicely():
    student = Student(1, "Test student", 2)
    assert str(student) == "Student(1, Test student, 2)"
    # Try commenting out the `__repr__` method in lib/student.py
    # And see what happens when you run this test again.


"""
We can compare two identical students
And have them be equal
"""


def test_students_are_equal():
    student1 = Student(1, "Test student", 3)
    student2 = Student(1, "Test student", 3)
    assert student1 == student2
    # Try commenting out the `__eq__` method in lib/student.py
    # And see what happens when you run this test again.
