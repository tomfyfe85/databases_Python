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
