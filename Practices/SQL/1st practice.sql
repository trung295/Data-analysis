--List the first 10 artists in the Artist table.
SELECT name FROM artist
limit 10;

--Retrieve the names and lengths (in milliseconds) of all tracks in the Track table.
SELECT name, Milliseconds as length FROM track;

--Find the names and composers of all tracks that belong to genre ID 1.
SELECT name, composer FROM Track
where GenreID = 1;

--Show all invoices from the Invoice table where the total is greater than 15.00.
SELECT * FROM Invoice 
where total > 15;

--List the 5 most expensive tracks by unit price.
SELECT name, UnitPrice  FROM Track 
order by UnitPrice desc
LIMIT 5;

--List all albums and the name of the artist who created each album.
SELECT title, name FROM Album 
inner join Artist 
	on Album.ArtistId = Artist.ArtistId
	
--Show all tracks and the names of the genres they belong to.
SELECT track.Name, genre.Name FROM Track 
inner join Genre 
	on Track.GenreId = Genre.GenreId
	
--Count the number of tracks in each genre. Display genre name and count.
SELECT Genre.Name , count(Track.Name ) as number_track FROM Genre
inner join Track
	on Genre.GenreId = Track.GenreId
group by Genre.Name 

--What is the total revenue (sum of Total) from each country?
SELECT BillingCountry , sum(invoice.Total) FROM Invoice
group by BillingCountry 

--Find all customers who are from the USA and have spent more than $20.
SELECT * from Customer
inner join Invoice
	on Customer.CustomerId = Invoice.CustomerId
where Invoice.Total > 20







