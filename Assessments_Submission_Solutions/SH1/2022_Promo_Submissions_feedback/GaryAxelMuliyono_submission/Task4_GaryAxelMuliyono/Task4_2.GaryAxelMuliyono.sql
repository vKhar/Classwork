SELECT Player.Name,AVG(Game.Score),COUNT(Player.PlayerID) FROM Player INNER JOIN Game ON Player.PlayerID = Game.PlayerID
-- need a GROUP BY for the aggregate function 