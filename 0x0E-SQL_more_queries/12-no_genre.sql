-- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_s.title, tv_s_genres.genre_id
FROM `tv_shows` AS tv_s
LEFT JOIN `tv_show_genres` AS tv_s_genres
ON tv_s.id = tv_s_genres.show_id
WHERE tv_s_genres.genre_id IS NULL
ORDER BY tv_s.title, tv_s_genres.genre_id;
