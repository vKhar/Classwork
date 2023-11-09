select Name, (sum(score)/count(gameID)) 
from Player,Game
INNER JOIN Game on PlayerID;