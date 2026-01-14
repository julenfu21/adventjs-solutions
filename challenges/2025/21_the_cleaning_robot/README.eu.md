<div align="center">
    <h1>Erronka #21: 🤖 Garbiketa-Robota</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Zailtasuna-ERTAINA-yellow" alt="Zailtasuna: Ertaina">
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

Bizarzizuriren biltegi bertikala modernizatu egin da! Orain, opariak zutabetan pilatzeaz gain, biltegian errenkada bat beteta egotekotan opariak jasotzen dituen robot 🤖 bat dago.

Biltegia `#` opariz eta `.` zuriunez osatutako matrize bat da. `clearGifts` funtzio bat sortu behar duzu, sarrera-parametro gisa biltegiaren uneko egoera eta opariak sartzeko zutabeen indizeak dituen zerrenda bat jasotzen dituena.

**Opariak sartzeko arauak:**

- Oparia zehaztutako zutabetik eta biltegiaren goiko ertzetik sartzen da.
- Oparia zutabe horretan **behetik hasita hutsik dagoen lehenengo gelaxkan (`.`)** kokatzen da.
- Zutabea beteta badago, oparia baztertu egiten da.

**Garbiketa-robotaren arauak:**

- Biltegian opari bat sartu ostean, errenkada bat opariz beteta geratzen bada (`#`), hura **desagertu** egiten da.
- Ezabatutako errenkadaren gainean zeuden gainontzeko errenkadak **1 posizio beherantz mugitzen dira**.
- Errenkada bat ezabatzen denean, errenkada huts berri bat (`.`) agertzen da goiko ertzean, biltegiaren tamaina mantentzeko.


## 💡 Adibideak

```js
clearGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['#', '.', '#']
  ],
  [1]
)
/*
1. Oparia 1 zutabean sartzen da
2. Errenkada 2k [# # #] balioa hartzen du
3. Errekada 2 beteta dago, robotak ezabatu egiten du
4. Errenkada huts berri bat erantsi da 0 posizioan

Result:
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['.', '.', '.']
]
*/

clearGifts(
  [
    ['.', '.', '#'],
    ['#', '.', '#'],
    ['#', '.', '#']
  ],
  [0, 1, 2]
)

/*
1. Oparia 0 zutabean sartzen da
2. Oparia 1 zutabean sartzen da
3. Errenkada 2k [# # #] balioa hartzen du
4. Errenkada 2 beteta dago, robotak ezabatu egiten du

Momentuz biltegiak honako itxura dauka:
[
  ['.', '.', '.']
  ['#', '.', '#'],
  ['#', '.', '#'],
]

5. Oparia 2 zutabean sartzen da

Result:
[
  ['.', '.', '#'],
  ['#', '.', '#'],
  ['#', '.', '#']
]
*/
```