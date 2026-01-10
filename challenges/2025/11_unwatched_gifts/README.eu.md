<div align="center">
    <h1>Erronka #11: 📹 Zaintzarik Gabeko Opariak</h1>
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

Grinch-ak gabonetako opariak lapurtu nahi ditu biltegitik. Horretarako, **zaintzarik gabeko opariak zeintzuk diren** jakin behar du.

Biltegia string-ez osatutako array batez (`string[]`) adierazita dago, non **opari bakoitza** (`*`) **babestuta egongo baita baldin eta kamera baten ondoan badago** (`#`). Zuriune bakoitza **puntu** (`.`) batez adierazita dago.

Zure egitekoa **zaintzarik gabeko oparien kopurua zenbatzea da**, hau da, oparien ondoko posizioetan (goian, behean, ezkerrean edo eskuinean) kamerarik ez duten oparien kopurua.

Honakoa kontuan izan: *4 noranzko kardinalak soilik hartzen dira "ondokotzat". Diagonalak, ez ordea.*

Izkinetan edo ertzetan dauden opariak zaintzarik gabe egon daitezke, baldin eta ondoan kamerarik ez badute.


## 💡 Adibideak

```js
findUnsafeGifts([
  '.*.',
  '*#*',
  '.*.'
]) // ➞ 0

// Opari guztiak kamera baten ondoan daude

findUnsafeGifts([
  '...',
  '.*.',
  '...'
]) // ➞ 1

// Opari honek ez du kamerarik inguruan

findUnsafeGifts([
  '*.*',
  '...',
  '*#*'
]) // ➞ 2
// Goi-ertzean dauden opariek ez dute kamerarik inguruan

findUnsafeGifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]) // ➞ 4

// Lau opariek ez dute kamerarik inguruan, kamerarekiko diagonalean daudelako
```