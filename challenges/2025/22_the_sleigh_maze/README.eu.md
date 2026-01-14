<div align="center">
    <h1>Erronka #22: 🎄 Leraren Labirintoa</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Zailtasuna-ZAILA-red" alt="Zailtasuna: Zaila">
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

Bizarzuri 🎅 **lera-simulagailu** bat probatzen ari da, biltegiaren barruan dagoen labirinto batean. Labirintoa karakterez osatutako matrize baten bidez adierazita dago.

Zure egitekoa ea abiapuntutik (`S`) irteeraraino (`E`) iris daitekeen egiaztatzen duen funtzio bat inplementatzea da.

**Labirintoaren arauak:**

- `S`: Bizarzuriren abiapuntua.
- `E`: Labirintoaren irteera.
- `.`: Oztoporik gabeko bidea.
- `#`: Pareta (bidea oztopatzen du).
- Baimendutako mugimenduak: **gora, behera, ezkerrera eta eskuinera**.


## 💡 Adibideak

```js
canEscape([
  ['S', '.', '#', '.'],
  ['#', '.', '#', '.'],
  ['.', '.', '.', '.'],
  ['#', '#', '#', 'E']
])
// → true

canEscape([
  ['S', '#', '#'],
  ['.', '#', '.'],
  ['.', '#', 'E']
])
// → false

canEscape([
  ['S', 'E']
])
// → true

canEscape([
  ['S', '.', '.', '.', '.'],
  ['#', '#', '#', '#', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', '#', '#', '#', '#'],
  ['.', '.', '.', '.', 'E']
])
// → true

canEscape([
  ['S', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#'],
  ['.', '.', 'E']
])
// → false
```

**Honakoa kontuan izan:**

- Egindako bidea itzultzea ez da beharrezkoa, labirintoaren irteeraraino iris daitekeen adieraztearekin nahikoa da.
- Bizarzuri ezin da labirintoaren mugetatik atera.
- Gelaxka beretik behin baino gehiagotan igaro daiteke.

**Aholkua**: Problema hau hainbat modutan ebaz daiteke, baina **BFS** (Breadth-First Search) edo **DFS** (Depth-First Search) bezalako bilaketa-algoritmoak ezin hobeak dira honelako erronketarako.