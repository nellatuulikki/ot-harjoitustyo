# Arkkitehtuurikuvaus

## Rakenne
Sovelluksen alustava rakenne on kolmitasoinen kerrosarkkitehtuuri.

Pakkaus ui sisältää käyttöliittymän, services sovelluslogiikan ja repositories sisältää tietokantoihin liittyvän koodin. Entities pakkaus sisältää sovelluksen käyttämiä luokkia.

## Käyttöliittymä

Tällä hetkellä kolme näkymää:
- Pelaajien nimien määrittely
- Pelinäkymä
- Valikkonäky
  
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

Sen jälkeen tapahtumakäsittelijä kutsuu sovelluslogiikan PlayService metodia create_players, joille annetaan parametriksi käyttäjän kirjoittamat pelaajien nimet ja ruudukon koko. Create_players metodi luo kaksi Player-oliota ja yhden Game-olion, joka saa parametreikseen juuri luodut kaksi Player oliota sekä ruudukon korkeuden ja leveyden. Tässä yhteydessä myös tietokantaan tallennetaan alustavat tiedot pelistä. Tämän jälkeen käyttöliittymä vaihtaa TicTacToeView:n ja peli voi alkaa.

![image](https://user-images.githubusercontent.com/94007460/147419478-2b3d7dd9-a660-4ecb-9180-673b41c67c90.png)



![image](https://user-images.githubusercontent.com/94007460/147419723-c67e4748-70cc-40be-b289-be832f74a703.png)


### Pelin loppuminen



