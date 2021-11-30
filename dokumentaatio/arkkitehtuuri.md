# Arkkitehtuurikuvaus

## Rakenne
Sovelluksen alustava rakenne on kolmitasoinen kerrosarkkitehtuuri. Pakkausrakenne on näyttää tältä:






Pakkaus ui sisältää käyttöliittymän, services sovelluslogiikan ja repositories sisältää tietokantoihin liittyvän koodin. Entities pakkaus sisältää sovelluksen käyttämiä luokkia.

## Käyttöliittymä

Tällä hetkellä kaksi näkymää:
  Pelaajien nimien määrittely
  Pelinäkymä
  
Näkymistä vastaa UI-luokka ja molemmat näkymät ovat tuotettu omina luokkinaan. Käyttöliittymää loudessa on pyritty siihen, että sovelluslogiikka olisi mahdollisimman eriytetty. 

## Sovelluslogiikka

![image](https://user-images.githubusercontent.com/94007460/144122858-00f06919-d692-415d-90e9-2247380f466a.png)
