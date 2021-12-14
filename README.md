# Ohjelmistotekniikka, harjoitustyö



## TicTacToe

Sovelluksen avulla kaksi pelaajaa voi pelata ristinollaa pelilaudalla. HUOM! Peli on muutettu suuremmalle pelilaudalle, ja tällä hetkellä pelilaudan koko täytyy olla vähintää 5x5. Rajoituksia pelilaudan kokoon ei kuitenkaan ole ehditty lisätä, joten voi olla että peli ei toimi optimaalisesti pienemmällä pelilaudalla.

## Dokumentaatio


[Arkkitehtuurikuvaus](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Vaatimuusmäärittely](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Käyttöohje](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testaus](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/testaus) 

[Release](https://github.com/nellatuulikki/ot-harjoitustyo/releases/tag/vk5)

## Sovelluksen asennus

### Aseta riippuvuudet 

  poetry install
  
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
 
