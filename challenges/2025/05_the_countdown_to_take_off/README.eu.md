<div align="center">
    <h1>Erronka #5: ⏱️ Aireratzerako Atzerako Kontaketa</h1>
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

Iratxoek **timestamp sekretu** bat daukate: **Bizarzuri lerarekin aireratzen den** 🛷 data eta ordu zehatza da, opariak mundu osoan zehar banatzeko. Baina Ipar Poloan formatu oso berezia erabiltzen dute ordua gordetzeko: `YYYY*MM*DD@HH|mm|ss NP` (adibidez: `2025*12*25@00|00|00 NP`).

Zure egitekoa sarrera-parametro gisa honakoa jasotzen duen funtzio bat idaztea da:

- `fromTime` → Erreferentzia-data iratxoen formatuan
- `takeOffTime` → Aireratze-data bera, iratxoen formatuan ere

Funtzioak honakoa itzuli behar du:

- Aireratzerako geratzen diren **segundo osoak**.
- Aireratze-unean bertan bagaude → `0`.
- Aireratzea dagoeneko gertatu bada → **zenbaki negatibo** bat, ordutik zenbat segundo igaro diren adieraziz.


## 📜 Arauak

- Hasteko, iratxoen formatuan dagoen data timestamp batean bihurtu. `NP` atzizkiak Ipar Poloko ordu ofiziala dela adierazten du (ordu-eremurik edo DST-rik gabe). Ondorioz, UTC balitz bezala erabili daiteke.
- Daten arteko aldea **segundotan** kalkulatu, ez milisegundotan.
- Beti beherantz biribildu (`floor`): segundo osoak soilik.


## 💡 Adibideak

```js
const takeoff = '2025*12*25@00|00|00 NP'

// 2025eko abenduaren 24tik, 23:59:30, aireratzea baino 30 segundo lehenago
timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)
// 30

// aireratze-unean bertan
timeUntilTakeOff('2025*12*25@00|00|00 NP', takeoff)
// 0

// aireratzea baino 12 segundo beranduago
timeUntilTakeOff('2025*12*25@00|00|12 NP', takeoff)
// -12
```