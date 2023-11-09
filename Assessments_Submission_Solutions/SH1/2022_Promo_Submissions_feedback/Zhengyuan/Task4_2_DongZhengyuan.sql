SELECT Player.Name, SUM(Game.Score), COUNT(Game.PlayerID) FROM Player 
INNER JOIN Game ON Game.PlayerID = Player.PlayerID
-- AVERAGE
-- GRIUO BY