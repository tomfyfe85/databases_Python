1. Extract nouns from the user stories or specification
# EXAMPLE USER STORIES:

As a blogger,
So I can organise my blog posts,
I want to keep a list of posts with their title and content.

As a blogger,
So I can organise my blog posts,
I want to keep a list of tags with their name (e.g 'coding' or 'travel').

As a blogger,
So I can organise my blog posts,
I want to be able to assign one tag to different posts.

As a blogger,
So I can organise my blog posts,
I want to be able to tag one post with one or different many tags.
Nouns:

posts, title, tags, name
2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
posts	title, content
tags	name
Name of the first table (always plural): posts

Column names: title, content

Name of the second table (always plural): tags

Column names: name

3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:
```sql
Table: posts
id: SERIAL
title: text
content: text

Table: tags
id: SERIAL
name: text
```

4. Design the Many-to-Many relationship
Make sure you can answer YES to these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
# EXAMPLE

1. Can one tag have many posts? YES
2. Can one post have many tags? YES
If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case.

5. Design the Join Table
The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is table1_table2.

# EXAMPLE

Join table for tables: posts and tags
Join table name: posts_tags
Columns: post_id, tag_id
6. Write the SQL.
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.
```sql
-- Create the first table.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

-- Create the second table.
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name text
);

-- Create the join table.
CREATE TABLE posts_tags (
  post_id int,
  tag_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (post_id, tag_id)
);
7. Create the tables.
psql -h 127.0.0.1 database_name < posts_tags.sql
````