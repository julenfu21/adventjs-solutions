<div align="center">
    <h1>Erronka #19: 🎄 Bizarzuriren Bidaia Sekretua</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-8%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Leraren GPS-a zoratu egin da! 😱 Bizarzurik **bere egin beharreko bidaiaren atalak** ditu, baina desordenaturik daude.

Zure egitekoa abiapuntutik helmugaraino **bide osoa berreraikitzea** da.

Honakoa aintzat hartu: **Array-ko lehenengo elementua beti bidaiaren lehenengo atala izango da**. Hortik aurrera, atalen helmugak hurrengo atalen abiapuntuekin lotu beharko dituzu.


## 💡 Adibideak

```js
revealSantaRoute([
  ['MEX', 'CAN'],
  ['UK', 'GER'],
  ['CAN', 'UK']
])
// → ['MEX', 'CAN', 'UK', 'GER']

revealSantaRoute([
  ['USA', 'BRA'],
  ['JPN', 'PHL'],
  ['BRA', 'UAE'],
  ['UAE', 'JPN'],
  ['CMX', 'HKN']
])
// → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']

revealSantaRoute([
  ['STA', 'HYD'],
  ['ESP', 'CHN']
])
// → ['STA', 'HYD']
```

🔎 **Honakoa kontuan izan:**

- Bizarzuriren bidean ez dago bikoiztutako biderik, ezta ziklorik ere.
- Baliteke bideari ez dagokiten atalen bat egotea; hauek baztertu egin behar dira.