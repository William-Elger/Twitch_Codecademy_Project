SELECT *
FROM chat
LIMIT 20;

SELECT *
FROM stream
LIMIT 20;

SELECT DISTINCT game
FROM stream;

SELECT DISTINCT channel
FROM stream;

SELECT game, COUNT(*)
FROM stream
GROUP BY  game
ORDER BY 2 DESC;

SELECT country AS 'Country', COUNT(*) AS 'No. of Viewers'
FROM stream
WHERE game LIKE 'League of Legends' AND country IS NOT NULL
GROUP BY country
ORDER BY 2 DESC
LIMIT 10;

SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

SELECT DISTINCT game,
	CASE
		WHEN game = 'League of Legends' 
			THEN 'MOBA'
		WHEN game = 'Dota 2' 
			THEN 'MOBA'
		WHEN game = 'Heroes of the Storm' 
			THEN 'MOBA'
		WHEN game = 'Counter-Strike: Global Offensive'
			THEN 'FPS'
		WHEN game = 'DayZ'
			THEN 'Survival'
		WHEN game = 'ARK: Survival Evolved'
			THEN 'Survival'
		ELSE 'Other'
	END AS 'genre',
	COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

SELECT time
FROM stream
LIMIT 10;

SELECT strftime('%H', time) AS 'hour_of_day', COUNT(*) AS 'views'
FROM stream
WHERE COUNTRY = 'US'
GROUP BY 1;

SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id
LIMIT 20;