CREATE TABLE `Player` (
	`PlayerID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT NOT NULL,
	`CountryCode`	TEXT NOT NULL,
	`Gender`	TEXT NOT NULL,
	`DateOfBirth`	TEXT NOT NULL,
	FOREIGN KEY(`CountryCode`) REFERENCES `Country`(`CountryCode`)
);

CREATE TABLE `Country` (
	`CountryCode`	TEXT NOT NULL,
	`CountryName`	TEXT NOT NULL,
	`PlayerID`	INTEGER,
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`),
	PRIMARY KEY(`CountryCode`)
);

CREATE TABLE `Game` (
	`GameID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`PlayerID`	INTEGER NOT NULL,
	`DatePlayed`	TEXT NOT NULL,
	`StartTime`	TEXT NOT NULL,
	`Score`	TEXT NOT NULL,
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`)
);