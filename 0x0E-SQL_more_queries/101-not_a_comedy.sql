-- This script lists all shows without the genre Comedy

SELECT title
FROM tv_shows
WHERE id NOT IN (
SELECT DISTINCT tsg.show_id
FROM tv_show_genres tsg
LEFT JOIN tv_genres tg
ON tg.id=tsg.genre_id
WHERE tg.name = 'Comedy')
ORDER BY title;
