CREATE TABLE `Country` (
	`CountryCode`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`CountryName`	TEXT,
	`CaptainID`	INTEGER,
	FOREIGN KEY(`CaptainID`) REFERENCES `Player`(`PlayerID`)
); -- [1]
CREATE TABLE `Player` (
	`PlayerID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`CountryCode`	TEXT,
	`Gender`	TEXT,
	`DateOfBirth`	TEXT,
	FOREIGN KEY(`CountryCode`) REFERENCES `Country`(`CountryCode`)
); -- [1]
CREATE TABLE `Game` (
	`GameID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`PlayerID`	INTEGER NOT NULL,
	`DatePlayed`	TEXT,
	`StartTime`	TEXT,
	`Score`	INTEGER,
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`)
); --[1]
-- [1] Correct FKs for Country -> Player, Player->CountryCode, Game -> Player