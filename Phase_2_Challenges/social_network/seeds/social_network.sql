-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  email text
);
-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  number_of_views int,
  -- The foreign key name is always {user}_id
  user_id int,
  constraint fk_user foreign key(user_id) references users(id) on delete cascade
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email)
VALUES ('tom', 'fyfe@keg.com');
INSERT INTO users (name, email)
VALUES ('chants', 'chants@twtw.com');
INSERT INTO users (name, email)
VALUES ('kipper', 'kipper@steak.com');
INSERT INTO posts (title, content, number_of_views, user_id)
VALUES ('new album!', 'PYRAMID POWER BABY!', 666, 1);
INSERT INTO posts (title, content, number_of_views, user_id)
VALUES ('new live show', 'we are on this week', 100, 2);
INSERT INTO posts (title, content, number_of_views, user_id)
VALUES (
    'el beers',
    'tour beers are good beers',
    110000,
    3
  );