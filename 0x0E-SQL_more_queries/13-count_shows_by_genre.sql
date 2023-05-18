-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_g.name AS genre,
COUNT(tv_s_genres.genre_id) AS number_of_shows
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_s_genres
ON tv_g.id = tv_s-genres.genre_id
GROUP BY tv_g.name
ORDER BY number_of_shows DESC;
