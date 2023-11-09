SELECT Player.PlayerName, COUNT(Game.PlayerID) FROM Player INNER JOIN Game ON Player.PlayerID=Game.PlayerID 

-- average ?, group by