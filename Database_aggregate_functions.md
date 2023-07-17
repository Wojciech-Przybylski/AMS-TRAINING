`select Continent, sum(population) as population_per_continent from country Group BY Continent;`
+---------------+--------------------------+
| Continent     | population_per_continent |
+---------------+--------------------------+
| North America |                482993000 |
| Asia          |               3705025700 |
| Africa        |                784475000 |
| Europe        |                730074600 |
| South America |                345780000 |
| Oceania       |                 30401150 |
| Antarctica    |                        0 |
+---------------+--------------------------+
