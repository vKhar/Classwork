SELECT Player.Name, AVG(Game.Score), COUNT(*) FROM Player
INNER JOIN GAME
ON Player.PlayerID=Game.PlayerID
GROUP by Player.Name