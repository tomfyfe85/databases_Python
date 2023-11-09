```python
## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python

# Table name: Albums

# Model class
# class Album
# (in lib/album.py)


# Repository class
# class AlbumRepository
# (in lib/album_repository.py)


```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Model class
# (in lib/albums.py)
class Albums():
  def __init__(self, title, release_year, artist_id):
    self.title = title
    self.release_year = release_year
    self.artist_id = artist_id
  
  def __eq__(self, other):
  return self.__dict__ == other.__dict__
  pass

  def __repr__(self): 
  return f"Artists({self.id}, {self.name}, {self.genre})"
  pass


        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class AlbumRepository():
    def __init__(self, connection):
      self.connection = connection
    # Selecting all records
    # No arguments
    def all():
      result = self.connection.execute("SELECT * FROM albums")
        # Executes the SQL query:
        # SELECT title, release_year, artist_id FROM albums
      albums = []
      for row in result:
        album = Album(row['title'], row['release_year'], row['artist_id'])
        albums.append(album)
      return artists
        # Returns an array of Album objects.
  

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

# Album class
"""
When I construct an Artist
With the fields id, name and genre
They are reflected in the instance props
"""

def test_constructs_with_fields()
  album = Album('Doolittle', 1989, 1)
  assert album.title == 'Doolittle'
  assert album.release_year == 1989
  assert album.artist_id == 1

"""
When I construct two artists with the same fields they
Are equal.
"""

def test_equality():
  album_1 = Album('Doolittle', 1989, 1)
  album_2 = Album('Doolittle', 1989, 1)
  assert album_1 == album_2

"""
When I construct an Artist
And I format it to a String
Then It comes out in a friendly format
"""

def test_formatting()

 album_1 = Album('Doolittle', 1989, 1)
 assert str(album_1) == "Album(Doolittle, 1989, 1)"

# AlbumRepository class

"""
When I call #all on the AlbumRepository
I get all the albums back in a list
"""

def test_list_all_artists(db_connection)
  db_connection.seed("seeds/music_library.sql")
  repo = AlbumRepository(db_connection)
  result = repo.all()
  assert result == [
    Albums('Doolittle', 1989, 1),  
    Albums('Surfer Rosa', 1988, 1),
    Albums('Waterloo', 1974, 2),
    Albums('Super Trouper', 1980, 2),
    Albums('Bossanova', 1990, 1),
    Albums('Lover', 2019, 3),
    Albums('Folklore', 2020, 3),
    Albums('I Put a Spell on You', 1965, 4),
    Albums('Baltimore', 1978, 4),
    Albums('Here Comes the Sun', 1971, 4),
    Albums('Fodder on My Wings', 1982, 4),
    Albums('Ring Ring', 1973, 2)
]
# # 2albums.py
# # Get a single student

# repo = StudentRepository()

# student = repo.find(1)

# student.id # =>  1
# student.name # =>  'David'
# student.cohort_name # =>  'April 2022'

# # Add more examples for each method
# ```

# Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->