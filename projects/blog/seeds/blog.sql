DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP SEQUENCE IF EXISTS posts_id_seq;
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  post_content text
);
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  author text,
  post_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, post_content)
VALUES ('post1', 'content1');
INSERT INTO posts (title, post_content)
VALUES ('post2', 'content2');
INSERT INTO posts (title, post_content)
VALUES ('post3', 'content3');
INSERT INTO posts (title, post_content)
VALUES ('post4', 'content4');
INSERT INTO comments (comment_content, author, post_id)
VALUES ('hi', 'author1', 1);
INSERT INTO comments (comment_content, author, post_id)
VALUES ('great', 'author2', 2);
INSERT INTO comments (comment_content, author, post_id)
VALUES ('yo', 'author3', 3);
INSERT INTO comments (comment_content, author, post_id)
VALUES ('siiccck', 'author4', 3);