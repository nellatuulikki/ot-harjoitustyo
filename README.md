# Ohjelmistotekniikka, harjoitustyö



## TicTacToe

Sovelluksen avulla kaksi pelaajaa voi pelata ristinollaa pelilaudalla, jonka koon pelaajat saavat päättää. Tällä hetkellä sovellus toimii pelilaudoilla, joka on vähintään 5x5 ja enintään 20x20. Pelaajat määrittelevät itselleen nimen, ja voivat seurata sovelluksesta mahdollista omaa sijoitustaan parhaimpien pelaajien joukossa. Sovellus myös näyttää viiden edellisen pelin statistiikat. Sovellus toimii Pythonin 3.8-versiolla.

## Dokumentaatio


[Arkkitehtuurikuvaus](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Vaatimuusmäärittely](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Käyttöohje](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testaus](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/testaus) 

[Release 1](https://github.com/nellatuulikki/ot-harjoitustyo/releases/tag/vk5)

[Release 2](https://github.com/nellatuulikki/ot-harjoitustyo/releases/tag/vk6)

## Sovelluksen asennus

### Aseta riippuvuudet 

  poetry install
  
### Suorita alustustoimenpiteet

  poetry run invoke build
  
### Käynnistä sovellus 
  
  poetry run invoke start
  
## Komentorivitoimintoja
 
### Sovelluksen ajo
 
  poetry run invoke start
 
### Sovelluksen testaus
 
  poetry run invoke test
  
### Testikattavuus raportin generointi
 
  poetry run invoke coverage-report
  
  raportti löytyy htmlcov-hakemistosta
  
### PyLint
  
  Tiedostossa .pylintrc olevat tarkistukset suoritetaan komennolla:
  
  poetry run invoke lint
 
