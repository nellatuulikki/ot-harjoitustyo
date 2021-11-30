# Ohjelmistotekniikka, harjoitustyö



## TicTacToe

Sovelluksen avulla kaksi pelaajaa voi pelata ristinollaa 3x3 pelilaudalla.

## Dokumentaatio


[Arkkitehtuurikuvaus](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Vaatimuusmäärittely](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/nellatuulikki/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

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
 
