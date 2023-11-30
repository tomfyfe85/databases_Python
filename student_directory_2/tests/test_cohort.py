from lib.cohort import Cohort

"""
Cohort constructs with an id, name and genre
"""


def test_cohort_constructs():
    cohort = Cohort(1, "Test Cohort", '2023-03-21')
    assert cohort.id == 1
    assert cohort.name == "Test Cohort"
    assert cohort.starting_date == '2023-03-21'


"""
We can format cohorts to strings nicely
"""


def test_cohorts_format_nicely():
    cohort = Cohort(1, "Test Cohort", '2023-03-21')
    assert str(cohort) == "Cohort(1, Test Cohort, 2023-03-21)"
    # Try commenting out the `__repr__` method in lib/cohort.py
    # And see what happens when you run this test again.


"""
We can compare two identical cohorts
And have them be equal
"""


def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Test Cohort", "2023-03-21")
    cohort2 = Cohort(1, "Test Cohort", '2023-03-21')
    assert cohort1 == cohort2
    # Try commenting out the `__eq__` method in lib/cohort.py
    # And see what happens when you run this test again.
