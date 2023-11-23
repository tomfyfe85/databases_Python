from lib.database_connection import DatabaseConnection
# from databases_repoClone_and_exercises.databases.Phase_2_Challenges.recipe_directory.lib.recipe_repository import ARepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes.sql")

# Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)
