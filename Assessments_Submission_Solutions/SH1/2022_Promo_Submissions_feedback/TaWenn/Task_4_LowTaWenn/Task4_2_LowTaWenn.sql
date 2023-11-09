select Player.Name, Game.GameID from Player
inner join Game
on Player.PlayerID = Game.PlayerID
