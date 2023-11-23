from lib.recipe import Recipe

"""
Recipe constructs with an id, name, cooking_time and rating
"""


def test_recipe_constructs():
    recipe = Recipe(1, "Test name", 5, 5)
    assert recipe.id == 1
    assert recipe.name == "Test name"
    assert recipe.cooking_time == 5
    assert recipe.rating_1_to_5 == 5


"""
We can format recipes to strings nicely
"""


def test_recipes_format_nicely():
    recipe = Recipe(1, "Test name", 3, 2)
    assert str(recipe) == "Recipe(1, Test name, 3, 2)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.


"""
We can compare two identical recipes
And have them be equal
"""


def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test Recipe", 70, 4)
    recipe2 = Recipe(1, "Test Recipe", 70, 4)
    assert recipe1 == recipe2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
