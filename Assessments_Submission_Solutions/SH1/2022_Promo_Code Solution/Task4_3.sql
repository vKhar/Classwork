SELECT Player.Name,AVG(Game.Score),COUNT(Player.PlayerID)
FROM Player INNER JOIN Game ON Player.PlayerID = Game.PlayerID
GROUP BY Player.Name
-- SELECT ATTRIBUTES [1]
-- AVG [1]
-- JOIN [1]
-- GROUP BY [1]