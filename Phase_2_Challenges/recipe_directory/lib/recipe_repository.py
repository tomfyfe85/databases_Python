from lib.recipe import Recipe

class RecipeRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["name"], row["cooking_time"], row["rating_1_to_5"])
            recipes.append(item)
        return recipes
        
    # Find a single artist by their id
    def find(self, recipe_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_id])
        row = rows[0]
        return  Recipe(row["id"], row["name"], row["cooking_time"], row["rating_1_to_5"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    # def create(self, artist):
    #     self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
    #                             artist.name, artist.genre])
    #     return None

    # # Delete an artist by their id
    # def delete(self, artist_id):
    #     self._connection.execute(
    #         'DELETE FROM artists WHERE id = %s', [artist_id])
    #     return None
