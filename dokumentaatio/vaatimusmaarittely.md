# Vaatimusmäärittely

## Sovelluksen tarkoitus

Ristinollan pelaaminen, jossa kaksi pelaajaa laittavat vuortotellen risti- ja nolla-merkkejä pelilaudalle ja jos pelaaja saa kolme samaa merkkiä peräkkäin vaakasuunnassa, pystysuunnassa tai peräkkäin hän voittaa pelin.

## Käyttäjät

Sovellus tarvitsee toimiakseen kahta käyttäjää. Myöhemmin on myös mahdollista, että sovellukseen pystyy kirjautumaan omilla tunnuksilla, jolloin pelaajan tietoja voidaan säilyttää tietokannassa.

## Perusversion toiminnallisuudet

### Ennen pelin alkua

- Pelaajat määrittelevät nimensä ja päättävät kumpaa puolta pelaavat (Pelaajan nimi voi olla vain 10 merkkiä pitkä)
- Pelialustan koko määritellään. Perusversiossa vaihtoehtona on vain 3x3 alusta

### Pelin aikana

- Ruudulle ilmestyy 3x3 peliruutu
- Pelaajat vuorottelen lisäävät omia merkkejään laudalle
- Peli loppuu, kun jompikumpi pelaajista saa 3 merkkiä tai pelilaudalla ei ole enää tyhjiä ruutuja

### Pelin loppuessa
- Ruudulle ilmestyy voittajan nimi
- Pelaajilta kysytään haluavatko he pelata uudestaan

## Jarkokehitysideat
- Pelaajat voivat itse määritellä pelilaudan koon
- Pelaajat pystyisivät luomaan sovellukseen käyttäjätunnuksen ja salasanan, joilla on mahdollista kirjautua sovellukseen uudestaan
- Sovellus tallentaa tietoja käyttäjätunnuksen luoneista pelaajista (esimerkiksi hävityt ja voitetut pelit)
- Pelaajien on mahdollista tarkastella miten he ovat pärjänneet 
 - Tilastoja voitaisiin tarkastella erilaisten kuvaajien ja taulukoiden avulla
- Pelaaja pystyy poistamaan käyttäjänsä sovelluksesta
