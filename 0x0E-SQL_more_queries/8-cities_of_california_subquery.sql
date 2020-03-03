-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
 	SELECT * 
    FROM hbtn_0d_usa 
    WHERE states.name = "California" AND cities(*)
    ORDER BY cities.id ASC; 