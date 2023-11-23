from lib.recipe import Recipe

"""
Recipe constructs with an id, name, cooking_time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test name", "Test cooking_time", "Test rating")
    assert recipe.id == 1
    assert recipe.name == "Test name"
    assert recipe.cooking_time == "Test cooking_time"
    assert recipe.rating_1_to_5 == "Test rating"

"""
We can format recipes to strings nicely
"""
def test_artists_format_nicely():
    recipe = Recipe(1, "Test name", "Test cooking_time", "Test rating")
    assert str(recipe) == "Recipe(1, Test name, Test cooking_time, Test rating)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

# """
# We can compare two identical artists
# And have them be equal
# """
# def test_artists_are_equal():
#     artist1 = Artist(1, "Test Artist", "Test Genre")
#     artist2 = Artist(1, "Test Artist", "Test Genre")
#     assert artist1 == artist2
#     # Try commenting out the `__eq__` method in lib/artist.py
#     # And see what happens when you run this test again.
