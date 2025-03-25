USE Virtual_Art_Gallery
SELECT * FROM Artists 
SELECT * FROM Artworks 
SELECT * FROM Categories 
SELECT * FROM Exhibitions 
SELECT * FROM ExhibitionArtworks 

--1. Retrieve the names of all artists along with the number of artworks they have in the gallery, and list them in descending order of the number of artworks.
SELECT Name, COUNT(a.ArtistID) AS no_of_artworks FROM Artists INNER JOIN Artworks a ON Artists.ArtistID = a.ArtistIDGROUP BY NameORDER BY no_of_artworks DESC --2. List the titles of artworks created by artists from 'Spanish' and 'Dutch' nationalities, and order them by the year in ascending order.SELECT a.Nationality, a1.Title FROM Artists aINNER JOIN Artworks a1 ON a.ArtistID = a1.ArtistIDWHERE a.Nationality IN ('Spanish', 'Dutch')ORDER BY a1.Year ASC --3. Find the names of all artists who have artworks in the 'Painting' category, and the number of artworks they have in this category.
SELECT (SELECT Name FROM Artists a WHERE a.ArtistID = t.ArtistID) AS Name, 
t.art_works FROM (SELECT a.ArtistID, count(c.Name) AS art_works FROM Artworks a
INNER JOIN Categories c 
ON a.CategoryID = c.CategoryID
WHERE c.Name = 'Painting'
GROUP BY a.ArtistID) t

--4. List the names of artworks from the 'Modern Art Masterpieces' exhibition, along with their artists and categories.
SELECT a.Title AS artwork_title, a1.Name AS artist_name, c.Name AS category FROM Exhibitions e
INNER JOIN ExhibitionArtworks ea ON e.ExhibitionID = ea.ExhibitionID
INNER JOIN Artworks a ON ea.ArtworkID = a.ArtworkID
INNER JOIN Artists a1 ON a.ArtistID = a1.ArtistID
INNER JOIN Categories c ON a.CategoryID = c.CategoryID
WHERE e.Title = 'Modern Art Masterpieces'

--5. Find the artists who have more than two artworks in the gallery
SELECT a.name, COUNT(a1.ArtistID) AS num_artworks FROM Artists a
INNER JOIN Artworks a1 ON a.ArtistID = a1.ArtistID
GROUP BY a.name
HAVING COUNT(a1.ArtistID) > 2

--6. Find the titles of artworks that were exhibited in both 'Modern Art Masterpieces' and 'Renaissance Art' exhibitions.
SELECT a.Title FROM ExhibitionArtworks ea
INNER JOIN ExhibitionArtworks ea1 ON ea.ArtworkID = ea1.ArtworkID
INNER JOIN Artworks a ON ea.ArtworkID = a.ArtworkID
WHERE ea.ExhibitionID = 1 AND ea1.ExhibitionID = 2;

--7. Find the total number of artworks in each category
SELECT a.CategoryID, COUNT(a.Title) AS num_artworks FROM Artworks a
GROUP BY a.CategoryID

--8. List artists who have more than 3 artworks in the gallery.
SELECT a1.Name, COUNT(a.ArtworkID) AS num_artworks FROM Artworks a
INNER JOIN Artists a1 
ON a.ArtistID = a1.ArtistID
group BY a1.Name
HAVING COUNT(a.ArtworkID) > 3

--9. Find the artworks created by artists from a specific nationality (e.g., Spanish).
SELECT a1.Title AS Artwork, a.Name AS Author_name, a.Nationality FROM Artists a
INNER JOIN Artworks a1 ON a.ArtistID = a1.ArtistID
WHERE a.Nationality = 'Spanish'

--10. List exhibitions that feature artwork by both Vincent van Gogh and Leonardo da Vinci.
SELECT * FROM Exhibitions e
INNER JOIN ExhibitionArtworks ea1 ON e.ExhibitionID = ea1.ExhibitionID
INNER JOIN Artworks a1 ON ea1.ArtworkID = a1.ArtworkID
INNER JOIN Artists ar1 ON a1.ArtistID = ar1.ArtistID
INNER JOIN ExhibitionArtworks ea2 ON e.ExhibitionID = ea2.ExhibitionID
INNER JOIN Artworks a2 ON ea2.ArtworkID = a2.ArtworkID
INNER JOIN Artists ar2 ON a2.ArtistID = ar2.ArtistID
WHERE ar1.Name = 'Vincent van Gogh' 
AND ar2.Name = 'Leonardo da Vinci';

