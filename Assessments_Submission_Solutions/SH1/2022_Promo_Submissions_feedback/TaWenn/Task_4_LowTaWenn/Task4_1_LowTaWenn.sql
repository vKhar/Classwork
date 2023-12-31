CREATE TABLE `Player` (
	`PlayerID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT NOT NULL,
	`CountryCode`	TEXT NOT NULL,
	`Gender`	TEXT NOT NULL,
	`DateOfBirth`	INTEGER NOT NULL,
	FOREIGN KEY(`CountryCode`) REFERENCES `Country`(`CountryCode`)

);
CREATE TABLE `Country` (
	`CountryCode`	TEXT NOT NULL,
	`CountryName`	TEXT NOT NULL,
	`PlayerID`	INTEGER NOT NULL,
	PRIMARY KEY(`CountryCode`),
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`)
);
CREATE TABLE `Game` (
	`GameID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`PlayerID`	INTEGER NOT NULL,
	`DatePlayed`	TEXT NOT NULL,
	`StartTime`	INTEGER NOT NULL,
	`Score`	INTEGER NOT NULL,
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`)
);
