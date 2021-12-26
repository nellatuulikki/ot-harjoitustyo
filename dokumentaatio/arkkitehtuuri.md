# Arkkitehtuurikuvaus

## Rakenne
Sovelluksen alustava rakenne on kolmitasoinen kerrosarkkitehtuuri.

Pakkaus ui sisältää käyttöliittymän, services sovelluslogiikan ja repositories sisältää tietokantoihin liittyvän koodin. Entities pakkaus sisältää sovelluksen käyttämiä luokkia.

## Käyttöliittymä

Tällä hetkellä kolme näkymää:
- Pelaajien nimien määrittely
- Pelinäkymä
- Valikkonäkymä
  
Näkymistä vastaa UI-luokka ja kaikki näkymät ovat tuotettu omina luokkinaan. Käyttöliittymää loudessa on pyritty siihen, että sovelluslogiikka olisi mahdollisimman eriytetty, ja se kutsuu vain PlayService-luokassa olevia metodeja.

## Sovelluslogiikka

Sovelluksen tietomalli koostuu kahdesta luokasta Player ja Game. Player luokka sisältää tiedot peliä pelaavista pelaajista ja Game sisältää tietoa itse pelistä.

![image](https://user-images.githubusercontent.com/94007460/147418836-2d0054a4-3dc3-4441-8ba1-5b72f0676799.png)


PlayService luokka vastaa sovelluslogiikasta ja se mahdollistaa käyttöliittymän pääsyn luokkiin Game ja Player. Myöhemmin kurssin aikana sovellukseen lisätään pakkaus repositories ja sen luokat GameRepository ja UserRepository.

![image](https://user-images.githubusercontent.com/94007460/144127917-12080828-1ad8-460d-9d0a-10b54aa061e1.png)

## Tietojen pysyväistallennus

Repositories luokat ovat vastuussa sovelluksessa luotujen tietojen tallennuksesta. PlayerRepository ja GameRepository tallentavat tietoja SQLite-tietokantaan. Pelaaja-tiedot tallennetaan players tauluun ja Peli-tiedot tallennetaan games-tauluun. Taulut ovat alustettu initialize_database.py-tiedostossa Luokissa on noudatettu Repository-suunnittelumallia.

## Päätoiminnallisuudet

Tässä alakohdassa esitetään muutama sovelluksen päätoiminallisuus

### Pelin luominen
Peli alkaa kun syötekenttiin on määritelty kaksi pelaajaa ja käyttäjä on painanut Start The Game näppäintä.

![image](https://user-images.githubusercontent.com/94007460/147419157-ae663132-e6ef-4fe1-b0bf-43b05b28d7ad.png)

Sen jälkeen tapahtumakäsittelijä kutsuu sovelluslogiikan PlayService metodia create_players, joille annetaan parametriksi käyttäjän kirjoittamat pelaajien nimet ja ruudukon koko. Create_players metodi luo kaksi Player-oliota ja yhden Game-olion, joka saa parametreikseen juuri luodut kaksi Player oliota sekä ruudukon korkeuden ja leveyden. Tämän jälkeen käyttöliittymä vaihtaa TicTacToeView:n ja alkaa näyttämään peliä ruudulla.

### Pelimerkin 

![image](https://user-images.githubusercontent.com/94007460/147419478-2b3d7dd9-a660-4ecb-9180-673b41c67c90.png)

Kun pelaaja painaa nappulaa ruudukolla tapahtumakäsittelijä kutsuu sovelluslogikaan player_1_move metodia, jossa on parametrina nappulan koordinaatit ruudukosta. Sovelluslogiikka kutsuu Game-olion metodia make_move, joka saa parametrina ruudukon ja pelaajan 1 merkin. Game-olion attribuutti move saa yhden arvon lisää. Game-olio tarkastaa get_game_status metodilla, onko ruudukossa 5 peräkkäistä merkkiä. PlayService havaitsee ettei pelissä ole voittajaa, ja palauttaa käyttöliittymälle tiedon että peliä ei ole voitettu ja peli voi jatkua. Pelin käyttöikkunaan ilmestyy nappulaan X-merkki.

### Pelin loppuminen

![image](https://user-images.githubusercontent.com/94007460/147419723-c67e4748-70cc-40be-b289-be832f74a703.png)

Kun pelaaja painaa nappulaa ruudukolla tapahtumakäsittelijä kutsuu sovelluslogikaan player_1_move metodia, jossa on parametrina nappulan koordinaatit ruudukosta. Sovelluslogiikka kutsuu Game-olion metodia make_move, joka saa parametrina ruudukon ja pelaajan 1 merkin. Game-olion attribuutti move saa yhden arvon lisää. Game-olio tarkastaa get_game_status metodilla, onko ruudukossa 5 peräkkäistä merkkiä. Nyt ruudukossa on 5 peräkkäistä, jolloin check_winner metodilla muutetaan winner attribuutti ajantasalle. PlayService havaitsee että pelissä on voittajaa ja tallentaa molempien pelaajien tietoihin tiedot hyviöstä ja voitosta. Sovelluslogiikka palauttaa käyttöliittymälle tiedon että peli on voitettu. Pelin näkymä vaihtuu game_ended_view:hin.

### Muut toiminnallisuudet

Pelin loppuessa Game-olion tiedot tallennetaan Games-tietokantaan. Jos palataan alkusivulle niin datasettien tiedot ovat muuttuneet vastamaan reaaliaikaista tilannetta.

## Ohjelman rakenteen heikkoudet

Jonkin verran toisteisuutta sovelluslogiikassa. Mietin myös olisiko pitänyt luoda oma erillinen tietomalli pelilaudalle.



