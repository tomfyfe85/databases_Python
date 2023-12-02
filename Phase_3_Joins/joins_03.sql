-- SELECT posts.id, posts.title
--   FROM posts 
--     JOIN posts_tags ON posts_tags.post_id = posts.id
--     JOIN tags ON posts_tags.tag_id = tags.id
--     WHERE tags.id = 2;

-- INSERT INTO tags (name) VALUES ('sql');
-- --inserted with id 5

-- INSERT INTO posts_tags (post_id, tag_id) VALUES(7, 5);

SELECT posts.id, posts.title
FROM posts
JOIN posts_tags ON posts_tags.post_id = posts.id
JOIN tags ON posts_tags.tag_id = tags.id
WHERE tags.id = 5;


-- use db joins_03