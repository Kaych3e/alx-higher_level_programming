-- List all genres from 'hbtn_0d_tvshows' and display number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column- 'genre', Second column - 'number_of_shows'
-- Dont display a genre that doesnt have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- Can use only one SELECT statement
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
	FROM tv_genres JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
