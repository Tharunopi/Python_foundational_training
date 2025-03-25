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
WHERE ar1.Name = 'Vincent van Gogh' AND ar2.Name = 'Leonardo da Vinci' AND ea1.ExhibitionID = ea2.ExhibitionID

--11. Find all the artworks that have not been included in any exhibition.SELECT a.ArtworkID, a.Title FROM Artworks aLEFT JOIN ExhibitionArtworks ea ON a.ArtworkID = ea.ArtworkIDWHERE ea.ExhibitionID IS NULL --12. List artists who have created artworks in all available categoriesSELECT DISTINCT(a3.Name) FROM Artworks aINNER JOIN Artworks a1 ON a.ArtworkID = a1.ArtworkIDINNER JOIN Artworks a2 ON a.ArtworkID = a1.ArtworkIDINNER JOIN Artists a3 ON a.ArtistID = a3.ArtistIDWHERE a.CategoryID = 1 AND a1.CategoryID = 2 AND a2.CategoryID = 3 --13. List the total number of artworks in each category.SELECT c.Name, COUNT(a.Title) AS num_artworks FROM Artworks aINNER JOIN Categories c ON a.CategoryID = c.CategoryIDGROUP BY c.Name--14. Find the artists who have more than 2 artworks in the gallerySELECT a1.Name, COUNT(a.Title) AS num_artworks FROM Artworks aINNER JOIN Artists a1 ON a.ArtistID = a1.ArtistIDGROUP BY a1.NameHAVING COUNT(a.Title) > 2--15. List the categories with the average year of artworks they contain, only for categories with more than 1 artwork.SELECT c.Name, AVG(Year) AS average FROM Artworks aINNER JOIN Categories c ON a.CategoryID = c.CategoryIDGROUP BY c.NameHAVING COUNT(year) > 1--16. Find the artworks that were exhibited in the 'Modern Art Masterpieces' exhibition.SELECT a.Title FROM ExhibitionArtworks eaINNER JOIN Exhibitions e ON ea.ExhibitionID = e.ExhibitionIDINNER JOIN Artworks a ON ea.ArtworkID = a.ArtworkIDWHERE e.Title = 'Modern Art Masterpieces'--17. Find the categories where the average year of artworks is greater than the average year of all artworks.SELECT c.Name, AVG(Year) AS average FROM Artworks aINNER JOIN Categories c ON a.CategoryID = c.CategoryIDGROUP BY c.NameHAVING AVG(a.year) > (SELECT AVG(Year) FROM Artworks)--18. List the artworks that were not exhibited in any exhibition.SELECT * FROM Artworks aLEFT JOIN ExhibitionArtworks ea ON a.ArtworkID = ea.ArtworkIDWHERE a.Title IS NULL--19. Show artists who have artworks in the same category as "Mona Lisa."SELECT a1.Name FROM Artworks a INNER JOIN Artists a1 ON a.ArtistID = a1.ArtistIDWHERE a.CategoryID = (SELECT a.CategoryID FROM Artworks aWHERE a.Title = 'Mona Lisa')--20. List the names of artists and the number of artworks they have in the gallery.SELECT a.Name, COUNT(a1.ArtworkID) AS num_artworks FROM Artists aINNER JOIN Artworks a1 ON a.ArtistID = a1.ArtistIDGROUP BY a.Name