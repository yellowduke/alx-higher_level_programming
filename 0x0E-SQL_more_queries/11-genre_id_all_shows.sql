-- Script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_s.title, tv_s_genres.genre_id
  FROM `tv_shows` AS tv_s
LEFT JOIN tv_show_genres AS tv_s_genres
ON tv_s.id = tv_s_genres.show_id
ORDER BY tv_s.title, tv_s_genres.genre_id;
