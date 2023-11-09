BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Player` (
	`PlayerID`	INTEGER NOT NULL UNIQUE,
	`CountryCode`	TEXT,
	`Gender`	TEXT,
	`DateOfBirth`	TEXT,
	`Name`	TEXT,
	FOREIGN KEY(`CountryCode`) REFERENCES `Country`(`CountryCode`),
	PRIMARY KEY(`PlayerID`)
);
CREATE TABLE IF NOT EXISTS `Game` (
	`GameID`	INTEGER NOT NULL UNIQUE,
	`PlayerID`	INTEGER,
	`DatePlayed`	TEXT,
	`StartTime`	TEXT,
	`Score`	INTEGER,
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`),
	PRIMARY KEY(`GameID`)
);
CREATE TABLE IF NOT EXISTS `Country` (
	`CountryCode`	TEXT NOT NULL UNIQUE,
	`CountryName`	TEXT,
	`PlayerID`	INTEGER,
	PRIMARY KEY(`CountryCode`),
	FOREIGN KEY(`PlayerID`) REFERENCES `Player`(`PlayerID`)
);
COMMIT;
