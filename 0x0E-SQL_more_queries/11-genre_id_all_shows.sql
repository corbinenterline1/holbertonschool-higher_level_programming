-- list all shows contained in hbtn_0d_tvshows, display NULL if no genre id
-- record display: tv_shows.title - tv_shows_genres.genre_id.
-- Ascending order by tv_shows.titles & tv_shows_genre.genre_id. 1 SELECT
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
