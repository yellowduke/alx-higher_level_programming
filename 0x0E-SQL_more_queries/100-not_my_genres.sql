-- A Query that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres AS tv_g
WHERE tv_genres.id NOT IN (
	SELECT tv_show_genres.genre_id
	FROM tv_shows AS tv_s
	INNER JOIN tv_show_genres AS tv_s_g
	ON tv_s.id = tv_s_g.show_id
       	WHERE tv_s.title = 'Dexter'
)
ORDER BY tv_g.name;
