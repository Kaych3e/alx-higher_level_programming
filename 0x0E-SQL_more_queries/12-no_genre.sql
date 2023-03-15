-- List all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record to display: tv_shows.title - tv_show_genres.genre_id
-- Results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
