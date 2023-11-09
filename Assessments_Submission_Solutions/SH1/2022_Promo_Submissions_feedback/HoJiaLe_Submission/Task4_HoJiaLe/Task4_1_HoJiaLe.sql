CREATE TABLE `Player` (
	`PlayerID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`CountryCode`	TEXT,
	`Gender`	TEXT,
	`DateOfBirth`	TEXT
);
CREATE TABLE `Country` (
	`CountryCode`	TEXT UNIQUE,
	`CountryName`	TEXT,
	`PlayerID`	INTEGER,
	PRIMARY KEY(`CountryCode`)
);
CREATE TABLE `Game` (
	`GameID`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`PlayerID`	INTEGER,
	`DatePlayed`	TEXT,
	`StartTime`	TEXT,
	`Score`	TEXT
    FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`)
);