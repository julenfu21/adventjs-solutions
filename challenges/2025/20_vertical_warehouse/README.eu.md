<div align="center">
    <h1>Erronka #20: 🎁 Biltegi Bertikala</h1>
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

Bizarzuren lantegian, iratxoak opariak 🎁 **biltegi bertikal** batean gordetzen ari dira. Opariak banan-banan sartzen dira zutabe jakin batean eta pixkanaka-pixkanaka pilatzen doaz.

Biltegia `#` opariz eta `.` zuriunez osatutako matrize bat da. `dropGifts` funtzio bat sortu behar duzu, sarrera-parametro gisa biltegiaren uneko egoera eta opariak sartzeko zutabeen indizeak dituen zerrenda bat jasotzen dituena.

**Opariak sartzeko arauak:**

- Oparia zehaztutako zutabetik eta biltegiaren goiko ertzetik sartzen da.
- Oparia zutabe horretan **behetik hasita hutsik dagoen lehenengo gelaxkan** (`.`) kokatzen da.
- Zutabea beteta badago, oparia baztertu egiten da.


## 💡 Adibideak

```js
dropGifts(
  [
    ['.', '.', '.'],
    ['.', '#', '.'],
    ['#', '#', '.']
  ],
  [0]
)
/*
[
  ['.', '.', '.'],
  ['#', '#', '.'],
  ['#', '#', '.']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['#', '#', '#']
  ],
  [0, 2]
)
/*
[
  ['#', '.', '.'],
  ['#', '#', '#'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
  ],
  [0, 1, 2]
)
/*
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['#', '#']
    ['#', '#']
  ],
  [0, 0]
)
/*
[
  ['#', '#']
  ['#', '#']
]
```