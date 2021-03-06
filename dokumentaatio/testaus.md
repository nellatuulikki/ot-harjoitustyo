
# Testausdokumentti

Ohjelmaa on kehityksen aikana testattu yksikkö ja integraatiotestein (unittest) sekä järjestelmätason testeillä

## Yksikkö ja integraatiotestaus

### Sovelluslogiikka

PlayService-luokka vastaa pelin sovelluslogiikasta, ja tätä testataan TestPlayService-testiluokalla. PlayService-oliolle injektoidaan riippuvuuksiksi repositorio-oliot, jotka tallentavat tietoa testien ajaksi pysyväistallennuksen sijaan. Repositio-oliot ovat nimetty FakeGameRepository ja FakePlayerRepository.

Sovelluslogiikkan testaus jäi jonkin verran kesken (kattavuus 81%) 

### Repositorio-luokat

Sovelluksessa on kaksi repositorio-luokkaa PlayerRepository ja GameRepository, ja niitä on testettu testeissä käytössä olleilla tiedostoilla, joiden nimet on konfiguroitu .env.test-tiedostoon. PlayerRepository luokan testattavuudesta vastaa TestPlayerRepository-testiluokka ja GameRepository luokan testattavuudesta vastaa TestGameRepository-testiluokka.

GameReposityn testikattavuudessa päästiin 100%, mutta PlayerRepositoryn oli hieman alhaisempi vain 86%.

### Testauskattavuus

Sovelluksen haaraumakattavuus on 93% (mukana ei ole käyttöliittymää).

Testauksen ulkopuolelle jäi build.py ja initialize_database.py, myöskin joissain tiedostoissa (kuten play_service.py ja player_repository) olisi pitänyt testatat vielä enemmän.

![image](https://user-images.githubusercontent.com/94007460/147418527-8c63816a-2580-4194-bc2b-c54cde1f4875.png)


## Järjestelmätestaus

# Asennus ja konfigurointi

Sovellusta on testattu eri releaseilla käyttöohjeen mukaan Linux-ympäristössä. 

# Toiminnallisuudet

Määrittelydokumentissa on merkitty kaikki kohdat, joihin sovellus pystyy tällä hetkellä. Syötekenttiä on testattu virheellisillä tiedoilla ja tarkastetty että virhetilanteissa sovellus toimii niin kuin pitää.

## Sovelluksen jääneet laatuongelmat

Sovellus on keskeneräinen seuraavissa asioissa
  Konfiguraatiossa määriteltyihin tiedostoihin ei ole luku/kirjoitusoikeuksia
  SQLite tietokantaa ei ole alustettu
  Pelilauta ei mukaudu optimaalisesti sovelluksen alustaan
  Pelin jälkeinen näkymä olisi vaatinut pientä kosmeettista muokkausta



