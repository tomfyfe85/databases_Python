test driving an all method on a repository class, in this case Artist


1) look at seeds file to see what fields the artist class has 
2) test a artist model class, this is used in the repo class
3) test artist repo class
4) 
```python
# test artist class
"""
When I construct an Artist
With the fields id, name and genre
They are reflected in the instance props
"""

def test_constructs_with_fields()
  artist = Artist(1, "The Beatles", "Rock")
  assert artist.id == 1
  assert artist.name ==  "The Beatles"
  assert artist.genre == "Rock"

"""
When I construct two artists with the same fields they
Are equal.
"""

def test_equality():
  artist_1 = Artist(1, "The Beatles", "Rock")
  artist_2 = Artist(1, "The Beatles", "Rock")
  assert artist_1 == artist_2

"""
When I construct an Artist
And I format it to a String
Then It comes out in a friendly format
"""

def test_formatting()


# create class

class Artist:
  def __init__(self, id, name, genre):
    self.id - id
    self.name = name
    self.genre = genre
    # test passes
    pass

# add this to add equality in testing IE even though the test
# ... case and database info with be from different instances
# ... if the contents is the same we are satisfied that they # ... are equal
  def __eq__(self, other):
    return self.__dict__ == other.__dict__
    pass

  # when str is used on an artist instance, a string like 
  # ... below is returned. IE str(artist) => 
  "Artists(1, Pixes, Rock)"
  def __repr__(self): 
    return f"Artists({self.id}, {self.name}, {self.genre})"
    pass

# test ArtistRepository class
"""
When I call all on the ArtistRepository
I get all the artists back in a list
"""
# need to connect to the database, use fixture db_connection
# import artist and artist_repo to file

def test_list_all_artists(db_connection)
# seed database to get sample data in
  db.connection.seed("seeds/music_library.sql")
  repo = ArtistRepository(db_connection)
  result = repo.all()
  #check seed fill to check what all should be
  assert result == [
    (1, 'Pixies', 'Rock');
    (2, 'ABBA', 'Pop');
    (3, 'Taylor Swift', 'Pop');
    (4, 'Nina Simone', 'Jazz');
  ]

# create class
# import Artist
class ArtistRepository:
  def __init__(self, connection)
      self.connection = connection
  
  # need to write some sql
  def all(self):
      result = self.connection.execute("SELECT * FROM artists")
      artists = []
      for row in result:
        item = Artist(row["id"], row["name"], row["genre"])
        artist.append(item)
      return artists

  

```
