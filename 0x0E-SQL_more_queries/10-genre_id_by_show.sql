-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_s.title, tv_s_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_s.id = tv_s_genres.show_id
ORDER BY tv_s.title ASC, tv_s_genres.genre_id ASC;
