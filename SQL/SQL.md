select title, release_year, length, rating from film where rating = 'PG' and title like '%AND%' order by length asc;
