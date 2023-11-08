-- From albums,
-- filter where id is '2',
-- and select only values for the columns id, title and release_year.
SELECT id, title, release_year
  FROM albums
  WHERE id = 2;

-- From albums,
-- filter where title is 'Doolittle',
-- and select only values for the columns id, title and release_year.

-- Make sure to always use single quotes ('')
-- to delimitate strings in conditions.
SELECT id, title, release_year
  FROM albums
  WHERE title = 'Doolittle';

-- We can use =, <, <=, >, >=
-- to compare values.

-- From albums,
-- filter where release_year is greater than 1990,
-- and select only values for the columns id, title and release_year.
SELECT id, title, release_year
  FROM albums
  WHERE release_year > 1990;

-- We can use the keywords AND and OR
-- to combine conditions.

-- From albums,
-- filter where release_year is greater than 1989 AND artist_id is '1',
-- and select only values for the columns id, title, release_year and artist_id.
SELECT id, title, release_year, artist_id
  FROM albums
  WHERE release_year > 1989 AND artist_id = 1;

--update
UPDATE [table_name] SET [column_name] = [new_value];
--eg
UPDATE albums SET title = 'A new title';
--specifically
UPDATE [table_name] SET [column_name] = [new_value]
  WHERE [conditions];

--eg
UPDATE albums
SET release_year = '2000', title = 'Whatever'
WHERE id = '1';
-- => release year updated to 2000 and title updated to 'Whatever'
-- WHERE id = '1'

--delete
DELETE FROM [table_name] WHERE [conditions];

-- Or, delete all records (never do this!)
DELETE FROM [table_name];

--create

INSERT INTO [table_name]
  ( [list of columns] )
  VALUES( [list of values] );

-- We don't specify the value for the `id`
-- column, the database will automatically pick one.
INSERT INTO artists 
  (name, genre)
  VALUES('Massive Attack', 'Alternative');

INSERT INTO albums (title, release_year)
VALUES ('Mezzanine', '1998');

UPDATE albums SET artist_id = '5'
WHERE title = 'Mezzanine';

--challenge

INSERT INTO artists
(name, genre)
VALUES('The Brothers Keg', 'Metal');

INSERT INTO albums
(title, release_year, artist_id)
VALUES('Folklore Myths and Legends...', '2020', '6')