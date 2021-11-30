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
