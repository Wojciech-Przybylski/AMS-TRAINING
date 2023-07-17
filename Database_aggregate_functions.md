`select Continent, sum(population) as population_per_continent from country Group BY Continent;`

output:

    | Continent     | population_per_continent |
    |------------------------------------------|
    | North America |                482993000 |
    | Asia          |               3705025700 |
    | Africa        |                784475000 |
    | Europe        |                730074600 |
    | South America |                345780000 |
    | Oceania       |                 30401150 |
    | Antarctica    |                        0 |

`select continent, max(Population) as max_population, min(Population) as min_population, avg(Population) as avg_population from country Group by continent;`

output:
    
    | continent     | max_population | min_population | avg_population |
    +---------------+----------------+----------------+----------------+
    | North America |      278357000 |           7000 |  13053864.8649 |
    | Asia          |     1277558000 |         286000 |  72647562.7451 |
    | Africa        |      111506000 |              0 |  13525431.0345 |
    | Europe        |      146934000 |           1000 |  15871186.9565 |
    | South America |      170115000 |           2000 |  24698571.4286 |
    | Oceania       |       18886000 |              0 |   1085755.3571 |
    | Antarctica    |              0 |              0 |         0.0000 |
    +---------------+----------------+----------------+----------------+
