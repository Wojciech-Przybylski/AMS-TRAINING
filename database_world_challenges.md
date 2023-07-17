`select count(name) from city where countrycode= 'USA';`

    | count(name) |
    ---------------
    |         274 |
`select population as population_of_Argentina from country where name= 'Argentina';`
    
    | population_of_Argentina |
    +-------------------------+
    |                37032000 |
    +-------------------------+

`select name, LifeExpectancy from country where LifeExpectancy != 'NULL' order by LifeExpectancy desc limit 10;`


    | name        | LifeExpectancy |
    +-------------+----------------+
    | Andorra     |           83.5 |
    | Macao       |           81.6 |
    | San Marino  |           81.1 |
    | Japan       |           80.7 |
    | Singapore   |           80.1 |
    | Australia   |           79.8 |
    | Switzerland |           79.6 |
    | Sweden      |           79.6 |
    | Hong Kong   |           79.5 |
    | Canada      |           79.4 |
    +-------------+----------------+

`Select country.name as Country, city.name as Capital_City from country left join city on city.id=country.capital where country.name= 'Spain';`

    | Country | Capital_City |
    +---------+--------------+
    | Spain   | Madrid       |
    +---------+--------------+

`Select distinct country.region, countrylanguage.Language from country left join countrylanguage on country.code=countrylanguage.countrycode where country.region= 'Southeast Asia' order by countrylanguage.language asc;`

    | region         | Language      |
    +----------------+---------------+
    | Southeast Asia | Bali          |
    | Southeast Asia | Banja         |
    | Southeast Asia | Batakki       |
    | Southeast Asia | Bicol         |
    | Southeast Asia | Bugi          |
    | Southeast Asia | Burmese       |
    | Southeast Asia | Cebuano       |
    | Southeast Asia | Chin          |
    | Southeast Asia | Chinese       |
    | Southeast Asia | Dusun         |
    | Southeast Asia | English       |
    | Southeast Asia | Hiligaynon    |
    | Southeast Asia | Iban          |
    | Southeast Asia | Ilocano       |
    | Southeast Asia | Javanese      |
    | Southeast Asia | Kachin        |
    | Southeast Asia | Karen         |
    | Southeast Asia | Kayah         |
    | Southeast Asia | Khmer         |
    | Southeast Asia | Kuy           |
    | Southeast Asia | Lao           |
    | Southeast Asia | Lao-Soung     |
    | Southeast Asia | Madura        |
    | Southeast Asia | Maguindanao   |
    | Southeast Asia | Malay         |
    | Southeast Asia | Malay-English |
    | Southeast Asia | Man           |
    | Southeast Asia | Maranao       |
    | Southeast Asia | Miao          |
    | Southeast Asia | Minangkabau   |
    | Southeast Asia | Mon           |
    | Southeast Asia | Mon-khmer     |
    | Southeast Asia | Muong         |
    | Southeast Asia | Nung          |
    | Southeast Asia | Pampango      |
    | Southeast Asia | Pangasinan    |
    | Southeast Asia | Pilipino      |
    | Southeast Asia | Portuguese    |
    | Southeast Asia | Rakhine       |
    | Southeast Asia | Shan          |
    | Southeast Asia | Sunda         |
    | Southeast Asia | Tamil         |
    | Southeast Asia | Thai          |
    | Southeast Asia | Tho           |
    | Southeast Asia | T?am          |
    | Southeast Asia | Vietnamese    |
    | Southeast Asia | Waray-waray   |
    +----------------+---------------+

`select country.name as country_name, city.name as city_name from city left join country on country.code=city.countrycode where city.name like 'F%' limit 25;`
    
    | country_name   | city_name                 |
    +----------------+---------------------------+
    | American Samoa | Fagatogo                  |
    | Argentina      | Florencio Varela          |
    | Argentina      | Formosa                   |
    | Botswana       | Francistown               |
    | Brazil         | Fortaleza                 |
    | Brazil         | Feira de Santana          |
    | Brazil         | Franca                    |
    | Brazil         | Florianópolis             |
    | Brazil         | Foz do Iguaçu             |
    | Brazil         | Ferraz de Vasconcelos     |
    | Brazil         | Francisco Morato          |
    | Brazil         | Franco da Rocha           |
    | Spain          | Fuenlabrada               |
    | India          | Faridabad                 |
    | India          | Firozabad                 |
    | India          | Farrukhabad-cum-Fatehgarh |
    | India          | Faizabad                  |
    | India          | Fatehpur                  |
    | Italy          | Firenze                   |
    | Italy          | Foggia                    |
    | Italy          | Ferrara                   |
    | Italy          | Forlì                     |
    | Japan          | Fukuoka                   |
    | Japan          | Funabashi                 |
    | Japan          | Fukuyama                  |
    +----------------+---------------------------+
