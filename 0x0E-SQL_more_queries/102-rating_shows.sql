-- This script lists all shows from 'hbtn_0d_tvshows_rate' by their rating.
-- Each record will display 'tv_shows.title' and their 'rating sum'.
-- Results will be sorted in descending order by their rating.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS `rating`
FROM tv_shows LEFT JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC
