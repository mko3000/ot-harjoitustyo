# Vaatimusmäärittely - Get This Bread

## Tarkoitus

Ohjelman tarkoituksena on toimia apuna hapanjuurileivän leipomisessa. Ohjelma mahdollistaa reseptien tallentamisen, reseptin vaiheittaisen suorituksen, automaattisen ajastimen odotusta vaativissa kohdissa, poikkeamien merkitsemisen reseptistä ja leivottujen leipien tallentamisen ja arvioimisen.

## Toiminnallisuus

Ohjelma tarjoaa seuraavan toiminnallisuuden:

- Reseptien tallentaminen (nimi, pvm, ainesosat, vaiheet)
- Dynaamien ainesosaluettelo
  - mahdollistaa leivän koon muuttamisen esim kaksinkertaiseksi, jolloin aieden määrät lasketaan automaattisesti
  - Yksikkömuunnin ainesosaluetteloon (SI <> amerikkalaiset yksiköt)
- Reseptin suoritus ajastimella
  - näyttää yhden vaiheen kerrallaan
  - kun tulee kohta, jossa pitää odottaa, käynnitää ajastimen
- Poikkeamien merkitseminen reseptistä
  - reseptiä suorittaessa käyttäjä voi merkitä, jos poikkesi reseptistä
- Leivotun leivän tallentaminen ja arvioiminen
- Uuden reseptin tallentaminen suorituksen perusteella
  - reseptin suorittamisen jälkeen, jos reseptistä on tehty poikkeamia, resptin voi tallentaa uutena reseptinä
- Helppokäyttöinen ja kivan näköinen käyttöliittymä

Ohjelman on aluksi tarkoitus toimia paikallisesti käyttäjän koneella, eikä käyttö vaadi kirjautumista tai mahdollista useiden käyttäjien käyttöä.

## Mahdolliset laajennukset

- Reseptien kategorisointi ja järjestäminen kansioihin
- Reseptien haku eri kriteerien perusteella (esim. leivonta-aika, ainesosat...)
- Verkkoalusta, jossa mahdollista
  - Käyttäjän reseptien jakaminen muille
  - Muiden käyttäjien leipien arvosteleminen
  - Pilvitallennus
  - Kuvien lisääminen leivistä
- Käyttäjäroolit peruskäyttäjille ja admin-rooli

