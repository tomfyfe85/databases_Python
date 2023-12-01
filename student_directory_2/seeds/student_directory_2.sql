DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date date
);
CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('June 22', '2023-06-01');
INSERT INTO cohorts (cohort_name, starting_date)
VALUES ('July 22', '2023-07-04');
INSERT INTO cohorts (cohort_name, starting_date)
VALUES ('August 22', '2023-09-03');
INSERT INTO students (student_name, cohort_id)
VALUES ('Tom', 1);
INSERT INTO students (student_name, cohort_id)
VALUES ('Chants', 3);
INSERT INTO students (student_name, cohort_id)
VALUES ('Viv', 1);
INSERT INTO students (student_name, cohort_id)
VALUES ('George', 2);