-- 1. How many tables does this database contain?
SELECT COUNT(*) 'Number of Tables' 
FROM sqlite_master
WHERE type='table'


-- 2. How many invoices are listed in this database?
SELECT count(invoiceid) 'Number Of Invoices'
FROM invoices

-- 3. Is there any customer with the name ‘John’?
SELECT count(FirstName) "John's"
FROM customers 
where customers.FirstName like '%John%'

-- 4. What is the longest album in the database?
SELECT albums.Title 'Album Title',max(tracks.Milliseconds) 'Lenght In Miliseconds'
FROM albums
JOIN tracks on tracks.AlbumId = albums.AlbumId

-- 5. What is the average length of a track in the database?
SELECT round(avg(tracks.Milliseconds),2) as 'Average Track Length'
FROM tracks

-- 6. What is the artist with more albums?
SELECT artists.ArtistId, artists.Name 'Artist Name', count(albums.albumId) 'Number of Albums'
FROM artists 
JOIN albums on albums.ArtistId = artists.ArtistId
GROUP by artists.Name
ORDER by count(albums.albumId) DESC
LIMIT 1

-- 7. List the top 5 artists with more sales.
SELECT ar.Name, round(sum(ii.UnitPrice),2) 'Total of Sales'
FROM invoice_items ii
JOIN tracks t on t.TrackId = ii.TrackId
JOIN albums al on al.AlbumId = t.AlbumId
JOIN artists ar on ar.ArtistId = al.ArtistId
GROUP by ar.Name
ORDER by sum(ii.UnitPrice) DESC
LIMIT 5


-- 8. List the tracks that contain ‘you’ in their title. List the album and artist of these
-- tracks.
SELECT t.Name SongName, al.Title Album, ar.name Artist
FROM tracks t
JOIN albums al on al.AlbumId = t.AlbumId
JOIN artists ar on ar.ArtistId = al.ArtistId
WHERE t.name like '%you%'

-- 9. What is the average number of items per invoice? List all invoices that have more
-- than the average number of items in them.

-- SELECT avg(ItemCount)
-- FROM (
-- 		SELECT count(TrackId) ItemCount
-- 		FROM invoice_items 
-- 		GROUP by InvoiceId)
------------------------------------------------
SELECT InvoiceId,count(TrackId)
FROM invoice_items 
GROUP by InvoiceId
HAVING count(TrackId) > ( 
	SELECT avg(ItemCount)
	FROM (
		SELECT count(TrackId) ItemCount
		FROM invoice_items 
		GROUP by InvoiceId)
		)

-- 10. How many invoices are there per year? What is the total amount in sales per
-- year?

SELECT strftime('%Y', InvoiceDate) Year, count(invoiceid) 'Amount of Invoices', sum(Total) 'Total of Sales'
FROM invoices 
GROUP by year
order by year

