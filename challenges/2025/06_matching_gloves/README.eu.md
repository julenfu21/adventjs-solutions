<div align="center">
    <h1>Erronka #6: 🧤 Eskularruak Parekatzen</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Zailtasuna-ERRAZA-brightgreen" alt="Zailtasuna: Erraza">
</p>
<br>


## 🌐 Beste Hizkuntza Batzuetan Irakurri

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Hizkuntza-es-yellow.svg" alt="Gaztelania" style="margin-right:16px;">
    </a>
    <a href="README.md">
        <img src="https://img.shields.io/badge/Hizkuntza-en-red.svg" alt="Ingelesa">
    </a>
</p>


## 💻 Inplementazioak eta Puntuazioak

| Programazio-Lengoaia | Puntuazioa | Inplementazioa |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Bizarzuriren lantegian, iratxoek guztiz nahastutako **eskularru magiko pilo bat** aurkitu dute. Eskularru bakoitza bi baliok deskribatzen dute:

- `hand`: ezkerreko (`L`) edo eskuineko (`R`) eskularrua den adierazten du
- `color`: eskularruaren kolorea (string)

Zure egitekoa eskularruak parekatzen laguntzea da: Bikote bat baliozkoa da baldin eta **kolore bereko** ezkerreko eta eskuineko eskularru batez osatuta badago.

Aurkitutako bikote guztien koloreak dituen zerrenda itzuli behar duzu. Kontuan izan **kolore bereko hainbat bikote egon daitezkeela**. Ordena, lehenago osatu daitekeen bikotearen arabera zehazten da.


## 💡 Adibideak

```js
const gloves = [
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'red' },
  { hand: 'R', color: 'green' },
  { hand: 'L', color: 'blue' },
  { hand: 'L', color: 'green' }
]

matchGloves(gloves)
// ["red", "green"]

const gloves2 = [
  { hand: 'L', color: 'gold' },
  { hand: 'R', color: 'gold' },
  { hand: 'L', color: 'gold' },
  { hand: 'L', color: 'gold' },
  { hand: 'R', color: 'gold' }
]

matchGloves(gloves2)
// ["gold", "gold"]

const gloves3 = [
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'green' },
  { hand: 'L', color: 'blue' }
]

matchGloves(gloves3)
// []

const gloves4 = [
  { hand: 'L', color: 'green' },
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'red' },
  { hand: 'R', color: 'green' }
]

matchGloves(gloves4)
// ['red', 'green']
```