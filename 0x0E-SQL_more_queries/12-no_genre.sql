-- list all shows with no genre linked
-- same order and shiz as last couple
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
