SELECT Name, SUM(Score)/COUNT(Score), COUNT(Score) 
FROM `Game` INNER JOIN `Player`
ON `Player`.PlayerID = `Game`.PlayerID 
GROUP BY Name;