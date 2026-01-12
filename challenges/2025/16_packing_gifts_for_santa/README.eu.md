<div align="center">
    <h1>Erronka #16: 🎁 Opariak Bizarzurirentzat Paketatzen</h1>
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

Bizarzurik opariak **ahalik eta modu eraginkorrenean** banatu nahi ditu. Oparien zerrenda bat, bakoitza bere **pisuarekin**, eta **pisu maximora arte** bete daitekeen trineoa dauzka.

Opariak **ordenan** banatzen dira eta Bizarzurik ezin du ordena aldatu. Opari bat uneko leran sartzen ez bada, Bizarzurik lera bidali eta beste lera berri bat prestatzen du.

Zure egitekoa beharrezko **lera kopuru minimoa** kalkulatzen duen funtzio bat idaztea da, opari guztiak banatu ahal izateko.

Hala ere, kontuan izan behar da batzuetan opariren bat ez dela lera batean ere ez sartuko. Kasu horretan `null` balioa itzuli behar da **leraren pisu maximoa** ez baita egokia opari zerrendarentzat.


## 💡 Adibideak

```js
packGifts([2, 3, 4, 1], 5)
// 2 lera
// 1. lera: 2 + 3 = 5
// 2. lera: 4 + 1 = 5

packGifts([3, 3, 2, 1], 3)
// 3 lera
// 1. lera: 3
// 2. lera: 3
// 3. lera: 2 + 1 = 3

packGifts([1, 1, 1, 1], 2)
// 2 lera
// 1. lera: 1 + 1 = 2
// 2. lera: 1 + 1 = 2

packGifts([5, 6, 1], 5)
// null
// 6 pisatzen duen opari bat dago eta ez da leran sartzen

packGifts([], 10)
// 0 lera
// Ez dago banatzeko oparirik
```