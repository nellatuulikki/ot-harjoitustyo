
# Käyttöohje

## Ennen Peliä

Asennetaan riippuvuudet komennolla

-   poetry install

Jonka jälkeen asennetaan alustustoimenpiteet:

-   poetry run invoke buils

Ohjelma käynnistetään

-   poetry run invoke start


## Pelaajien valinta

Sovelluksen alkaessa näytölle ilmestyy käyttöliittymä, josta pelaajat voivat nimetä itsensä ja määritellä pelilaudan koon. Nimi ei saa olla yli 10 merkkiä pitkä ja pelilaudan koko tulee määritellä kokonaisluvuilla alkaen 5x5 pelilaudasta aina 20x20 pelilautaan. Peli alkaa 'Start the game'-nappulan painalluksesta.

![image](https://user-images.githubusercontent.com/94007460/147417660-2891012e-f875-4d97-832d-b5c49f322939.png)


## Pelin aikana

Peli alkaa tyhjältä pelilaudalta. Pelissä määritellään kaksi pelaajaa, jotka vuorotellen painavat pelilaudan nappuloita. Pelaaja 1 pelaa risti-merkeillä ja Pelaaja 2 pelaa nolla-merkeillä. Pelaaja 1 aloittaa aina pelin. Pelilaudalla olevaa nappulaa painamalla voi merkitä ruudun omalle merkille.

![image](https://user-images.githubusercontent.com/94007460/146065690-eab9ec89-3b93-47f3-a8d9-aaf62d260c59.png)

Yhteen boksiin voi merkitä vain yhden merkin, ja peli ilmoittaa, jos boxissa on jo merkki.

![image](https://user-images.githubusercontent.com/94007460/146065972-c17e837e-d448-4a39-938e-dad6f8018b25.png)

Peli loppuu kun jompikumpi on saanut 5 merkkiä peräkkäin joko pysty-, vaaka- tai vinoriveille tai pelilauta on täynnä merkkejä. 

## Pelin loppuessa

Pelin loppuessa tulee 5 sekunnin viive ennen kuin peli siirtyy näytölle, josta saa valita haluavatko pelaajat pelata uudelleen vai haluatko he palata etusivulle. 

![image](https://user-images.githubusercontent.com/94007460/146065903-9faa8d41-d22f-43cc-b473-a6a52a3e1760.png)

