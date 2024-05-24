-- This script lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT tg.name AS name,
SUM(tsr.rate) AS rating
FROM tv_show_ratings tsr
RIGHT JOIN tv_show_genres tsg
ON tsg.show_id=tsr.show_id
LEFT JOIN tv_genres tg
ON tg.id=tsg.genre_id
GROUP BY tg.name
ORDER BY rating DESC;
