USE Virtual_Art_Gallery

-- Create the Artists table
CREATE TABLE Artists (
	ArtistID INT PRIMARY KEY,
	Name VARCHAR(255) NOT NULL,
	Biography TEXT,
	Nationality VARCHAR(100)
	)

-- Create the Categories table
CREATE TABLE Categories (
	CategoryID INT PRIMARY KEY,
	Name VARCHAR(100) NOT NULL
	)

-- Create the Artworks table
CREATE TABLE Artworks (
	ArtworkID INT PRIMARY KEY,
	Title VARCHAR(255) NOT NULL,
	ArtistID INT,
	CategoryID INT,
	Year INT,
	Description TEXT,
	ImageURL VARCHAR(255),
	FOREIGN KEY (ArtistID) REFERENCES Artists (ArtistID),
	FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
 )

-- Create the Exhibitions table
CREATE TABLE Exhibitions (
	ExhibitionID INT PRIMARY KEY,
	Title VARCHAR(255) NOT NULL,
	StartDate DATE,
	EndDate DATE,
	Description TEXT
 )

-- Create a table to associate artworks with exhibitions
CREATE TABLE ExhibitionArtworks (
 ExhibitionID INT,
 ArtworkID INT,
 PRIMARY KEY (ExhibitionID),
 FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions (ExhibitionID),
 FOREIGN KEY (ArtworkID) REFERENCES Artworks (ArtworkID)
 )