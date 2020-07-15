-- list all genres from hbtn_0d_tvshows & display # of shows linked to each
-- Record displays: <TV Show genre> - <Number of shows linked to this genre>
-- first column called genre, second number_of_shows. No genres with no shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_genres JOIN tv_show_genres WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id ORDER BY number_shows DESC;
