from lib.recipe_repository import RecipeRepository
from lib.recipe import (
    Recipe,
)

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""


def test_get_all_recipes(
    db_connection,
):  # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql")  # Seed our database with some test data
    repository = RecipeRepository(db_connection)

    recipes = repository.all()  # Get all recipes

    # Assert on the results
    assert recipes == [
        Recipe(1, "Pizza", 5, 5),
        Recipe(2, "Pasta", 15, 3),
        Recipe(3, "Ribs", 2040, 4),
    ]


# """
# When we call ArtistRepository#find
# We get a single Artist object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)

#     artist = repository.find(3)
#     assert artist == Artist(3, "Taylor Swift", "Pop")
