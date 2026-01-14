<div align="center">
    <h1>Erronka #25: 🪄 Hizkuntza Magikoa Egikaritu</h1>
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

Dagoeneko opari guztiak banatu ditugu! Bestalde, tailerrean, datorren urterako prestakizunekin hasi dira jada.

Iratxo jeinu bat programazio-lengoaia magiko bat 🪄 sortzen ari da, 2025ean umeei opariak banatzeko prozesua hobetzen lagunduko duena.

Programak beti `0` balioarekin hasten dira eta lengoaia string bat da, non karaktere bakoitzari agindu bati dagokion:

- `>` Hurrengo agindura mugitzen da
- `+` Uneko balioari 1 gehitzen dio
- `-` Uneko balioari 1 kentzen dio
- `[` eta `]`: Begizta. Uneko balioa `0` bada, `]` sinboloaren ondorengo agindura jauzi egiten du. Bestela, `[` sinboloaren ondorengo agindura itzultzen da.
- `{` eta `}`: Baldintza. Uneko balioa `0` bada, `}` sinboloaren ondorengo agindura jauzi egiten du. Bestela, programak  `{` sinboloaren ondorengo aginduan jarraitzen du.

Agindu guztiak exekutatu ostean lortutako balioa itzuli behar duzu.

**Oharra: Baldintza batek barruan begizta bat izan dezake, eta begizta batek barruan baldintza bat izan dezake. Hala ere, begizta batek barruan ez du sekula beste begizta bat izango, ezta baldintza batek beste baldintza bat barruan ere.**


## 💡 Adibideak

```js
execute('+++') // 3
execute('+--') // -1
execute('>+++[-]') // 0
execute('>>>+{++}') // 3
execute('+{[-]+}+') // 2
execute('{+}{+}{+}') // 0
execute('------[+]++') // 2
execute('-[++{-}]+{++++}') // 5
```