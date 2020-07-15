 # 0x0E - SQL - More queries
Task # | Short Description
-------|------------
[Task 0](0-privileges.sql) | Lists all privileges of the MySQL users `user_0d_1` & `user_0d_2` on `localhost`.
[Task 1](1-create_user.sql) | Creates the MySQL server user `user_0d_1`. All privileges, set password to `user_0d_1_pwd`.
[Task 2](2-create_read_user.sql) | Creates the database `hbtn_0d_2` & the user `user_0d_2`. Select privileges for the new user. NO FAILURES.
[Task 3](3-force_name.sql) | Creates the table `force_name` on your MySQL server.
[Task 4](4-never_empty.sql) | Creates the table `id_not_null` on your MySQL server.
[Task 5](5-unique_id.sql) | Creates the table `unique_id` on your MySQL server.
[Task 6](6-states.sql) | Creates the database `hbtn_0d_usa` & the table `states` in said database on your MySQL server.
[Task 7](7-cities.sql) | Creates the database `hbtn_0d_usa` & the table `cities` in said database on your MySQL server.
[Task 8](8-cities_of_california_subquery.sql) | Lists all the cities of California that can be found in the database `hbtn_0d_usa`. Sorted results, no `JOIN`.
[Task 9](9-cities_by_state_join.sql) | Lists all cities contained in the database `hbtn_0d_usa`. Records display as `cities.id` - `cities.name` - `states.name`.
[Task 10](10-genre_id_by_show.sql) | Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. Sorted results, only one `SELECT` statement.
[Task 11](11-genre_id_all_shows.sql) | Lists all shows contained in the database `hbtn_0d_tvshows`.
[Task 12](12-no_genre.sql) | Lists all shows contained in the `hbtn_0d_tvshows` without a genre linked. Sorted results, only one `SELECT` statement.
[Task 13](13-count_shows_by_genre.sql) | Lists all genres from `hbtn_0d_tvshows` & displays the number of shows linked to each.
[Task 14](14-my_genres.sql) | Lists all genres of the show `Dexter` from database `hbtn_0d_tvshows`.
[Task 15](15-comedy_only.sql) | Lists all Comedy shows from database `hbtn_0d_tvshows`. Sorting and such.
[Task 16](16-shows_by_genre.sql) | Lists all shows, & all genres to that show, from the database `hbtn_0d_tvshows`.
 ## Lessons Learned
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What's a `PRIMARY KEY`
* What's a `FOREIGN KEY`
* How to use `NOT NULL` and `UNIQUE` constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are `JOIN` and `UNION`
