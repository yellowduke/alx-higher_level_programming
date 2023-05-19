-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_s.title
FROM tv_shows AS tv_s
INNER JOIN tv_show_genres AS tv_s_g
ON tv_s.id = tv_s_g.show_id

INNER JOIN tv_genres AS tv_g
ON tv_g.id = tv_s_g.genre_id
WHERE tv_g.name = "Comedy"
ORDER BY tv_s.title;
