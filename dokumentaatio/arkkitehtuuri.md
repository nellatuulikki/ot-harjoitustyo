# Arkkitehtuurikuvaus

## Rakenne
Sovelluksen alustava rakenne on kolmitasoinen kerrosarkkitehtuuri.

Pakkaus ui sisältää käyttöliittymän, services sovelluslogiikan ja repositories sisältää tietokantoihin liittyvän koodin. Entities pakkaus sisältää sovelluksen käyttämiä luokkia.

## Käyttöliittymä

Tällä hetkellä kaksi näkymää:
  Pelaajien nimien määrittely
  Pelinäkymä
  
Näkymistä vastaa UI-luokka ja molemmat näkymät ovat tuotettu omina luokkinaan. Käyttöliittymää loudessa on pyritty siihen, että sovelluslogiikka olisi mahdollisimman eriytetty. 

## Sovelluslogiikka

Sovelluksen tietomalli koostuu kahdesta luokasta Player ja Game. Player luokka sisältää tiedot peliä pelaavista pelaajista ja Game sisältää tietoa itse pelistä.

![image](https://user-images.githubusercontent.com/94007460/144122858-00f06919-d692-415d-90e9-2247380f466a.png)

Playservice luokka vastaa sovelluslogiikasta ja se mahdollistaa käyttöliittymän pääsyn luokkiin Game ja Player. Myöhemmin kurssin aikana sovellukseen lisätään pakkaus repositories ja sen luokat GameRepository ja UserRepository.

![image](https://user-images.githubusercontent.com/94007460/144127917-12080828-1ad8-460d-9d0a-10b54aa061e1.png)


## Päätoiminnallisuudet

Tässä alakohdassa esitetään muutama sovelluksen päätoiminallisuus

### Pelin luominen
Peli alkaa kun syötekenttiin on määritelty kaksi pelaajaa ja käyttäjä on painanut Start The Game näppäintä.

![image](https://user-images.githubusercontent.com/94007460/145107172-d5790c39-ed20-46e9-9f0d-ca2ac1cea0dd.png)

Sen jälkeen tapahtumakäsittelijä kutsuu sovelluslogiikan PlayService metodia create_player, joille annetaan parametriksi käyttäjän kirjoittamat pelaajien nimet ja automaattisesti numero 3 (pelilaudan automaattinen koko sovelluksen perustoiminnallisuudessa). Create_players metodi luo kaksi Player-oliota ja yhden Game-olion, joka saa parametreikseen juuri luodut kaksi Player oliota sekä numeron 3. Tässä yhteydessä myös tietokantaan tallennetaan alustavat tiedot pelistä. Tämän jälkeen käyttöliittymä vaihtaa TicTacToeView:n ja peli voi alkaa.
