-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.name AS genre, tv_show_genres.genre_id AS number_of_shows
COUNT(*) IF NOT NULL
FROM tv_show_genres
GROUP BY genre, number_of_shows
HAVING COUNT(*) > 1;
ORDER BY number_of_shows DESC;
