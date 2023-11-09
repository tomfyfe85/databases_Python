from lib.album import Album

"""
When I construct an Album
With the fields id, name and genre
They are reflected in the instance props
"""

def test_constructs_with_fields():
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

def test_formatting():

  album_1 = Album('Doolittle', 1989, 1)
  assert str(album_1) == "Album(Doolittle, 1989, 1)"