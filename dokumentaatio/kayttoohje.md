
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

![image](https://user-images.githubusercontent.com/94007460/147417682-be094b5f-444b-4643-b118-e2bd4c0d1dae.png)

Yhteen boksiin voi merkitä vain yhden merkin, ja peli ilmoittaa, jos boxissa on jo merkki.

![image](https://user-images.githubusercontent.com/94007460/147417696-59c444fe-76ee-4311-a2cc-2502ae7a9344.png)


Peli loppuu kun jompikumpi on saanut 5 merkkiä peräkkäin joko pysty-, vaaka- tai vinoriveille tai pelilauta on täynnä merkkejä. 

## Pelin loppuessa

Pelin loppuessa tulee 5 sekunnin viive ennen kuin peli siirtyy näytölle, josta saa valita haluavatko pelaajat pelata uudelleen vai haluatko he palata etusivulle. 

![image](https://user-images.githubusercontent.com/94007460/147417721-bdbbc064-1d64-4187-a83c-e06d68f181c3.png)

Jos sovellus ohjataan takaisin etusivulle, pelin tiedot näkyvät viimeisimpien 5 pelin joukossa. Jos pelaajat ovat olleet hyviä, heidän nimensä saattaa ilmestyä myös Top 5 pelaajien listalle. Alla esimerkki, miltä datat näyttvät kuin pelejä on pelattu vain yksi.

![image](https://user-images.githubusercontent.com/94007460/147417765-220e51ca-c9c0-44c5-b320-39a8ac460f25.png)

