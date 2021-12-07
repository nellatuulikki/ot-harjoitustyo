
# Käyttöohje

## Ennen Peliä

Aja komento ennen itse sovelluksen ajoa

poetry install

Ohjelma käynnistetään

poetry run invoke start

## Pelin aikana

Peli alkaa tyhjältä pelilaudalta. Pelissä määritellään kaksi pelaajaa, jotka vuorotellan painavat pelilaudan nappuloita. Pelaaja 1 pelaa risti-merkeillä ja Pelaaja 2 pelaa nolla-merkeillä. Pelaaja 1 aloittaa aina pelin. Pelilaudalla olevaa nappulaa painamalla voi merkitä ruudun omalle merkille. Peli loppuu kun jompikumpi on saanut kolme merkkiä peräkkäin joko pysty-, vaaka- tai vinoriveille tai pelilauta on täynnä. Pelin loppuessa tulee 5 sekunnin viive ennen kuin peli siirtyy näytölle, josta saa valita haluavatko pelaajat pelata uudelleen vai haluatko he palata etusivulle.
