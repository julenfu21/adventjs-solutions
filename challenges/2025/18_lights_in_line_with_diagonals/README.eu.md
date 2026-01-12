<div align="center">
    <h1>Erronka #18: 🎄 Argiak Lerroan Diagonalekin</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-8%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Gabonetako argien panelak 🎄✨ sekulako arrakasta izan du. Hala ere, iratxoek haratago iritsi nahi dute: orain ea **diagonaletan** ere **kolore bereko 4 argiz osatutako lerrrorik** dagoen jakin nahi dute.

Panela berriro ere **matrize** baten bidez adierazita dago eta gelaxka bakoitzak honako balioak har ditzake:

- `'.'` → argi itzalia
- `'R'` → argi gorria
- `'G'` → argi berdea

Orain, zure funtzioak `true` itzuli behar du baldin eta piztuta dauden kolore bereko 4 argiz osatutako lerrorik badago, bai **norabide horizontalean ↔, bai bertikalean ↕ eta bai diagonalean ↘↙ ere**


## 💡 Adibideak

```js
hasFourInARow([
  ['R', '.', '.', '.'],
  ['.', 'R', '.', '.'],
  ['.', '.', 'R', '.'],
  ['.', '.', '.', 'R']
])
// true → 4 argi gorrik ↘ lerro diagonal bat osatzen dute

hasFourInARow([
  ['.', '.', '.', 'G'],
  ['.', '.', 'G', '.'],
  ['.', 'G', '.', '.'],
  ['G', '.', '.', '.']
])
// true → 4 argi berdek ↙ lerro diagonal bat osatzen dute

hasFourInARow([
  ['R', 'R', 'R', 'R'],
  ['G', 'G', '.', '.'],
  ['.', '.', '.', '.'],
  ['.', '.', '.', '.']
])
// true → 4 argi gorrik lerro horizontal bat osatzen dute

hasFourInARow([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → ez dago kolore bereko 4 argiz osatutako lerrorik
```

**Oharra:** Taularen tamaina edozein izan daiteke.