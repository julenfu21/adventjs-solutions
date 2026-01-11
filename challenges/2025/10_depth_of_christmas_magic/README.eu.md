<div align="center">
    <h1>Erronka #10: 📨 Gabonetako Magiaren Sakonera</h1>
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

🎄 Gabonetako Magiaren Sakonera

Ipar Poloan Bizarzuri mundutik zehar haur guztiengandik jasotzen dituen eskutitz magikoak aztertzen ari da 📩✨. Eskutitz hauek antzinako gabonetako hizkuntza batean idatzita daude, non `[` eta `]` kortxeteek gurarien intentsitatea adierazten duten.

Kortxeteen habiaraketa maila zenbat eta sakonagoa izan, orduan eta biziagoa izango da guraria. Zure egitekoa kortxeteen `[]` habiaraketaren **sakonera maila maximoa** aurkitzea da.

Baina kontuz ibili! Eskutitz batzuk **gaizki idatzita** egon daitezke. Kortxeteen proportzioa orekatuta ez badago (bat ireki baino lehenago ixten bada, ixte-kortxete batzuk soberan badaude edo ixte-kortxete batzuk falta badira), eskutitza baliogabea da eta `-1` itzuli behar da.


## 💡 Adibideak

```js
maxDepth('[]') // -> 1
maxDepth('[[]]') // -> 2
maxDepth('[][]') // -> 1
maxDepth('[[][]]') // -> 2
maxDepth('[[[]]]') // -> 3
maxDepth('[][[]][]') // -> 2

maxDepth('][') // -> -1 (ireki baino lehenago ixten da)
maxDepth('[[[') // -> -1 (ixte-kortxeteak falta dira)
maxDepth('[]]]') // -> -1 (ixte-kortxete batzuk soberan daude)
maxDepth('[][][') // -> -1 (kortxete bat itxi gabe dago)
```