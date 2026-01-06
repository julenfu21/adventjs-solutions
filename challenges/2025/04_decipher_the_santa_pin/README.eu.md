<div align="center">
    <h1>Erronka #4: 🧮 Bizarzuriren PIN-a Deszifratu</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-6%2F8-lightcoral" alt="Puntuazioa: 5-6" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Iratxoek Bizarzuriren lantegia babesten duen **kode zifratua** aurkitu dute 🔐. PIN-ak **4 digitu** ditu eta honelako blokeen barruan ezkutatuta dago:

```
[1++][2-][3+][<]
```

**Kodea abiapuntutzat hartuta, PIN-a deszifratzen duen funtzio bat idatz ezazu.**

Kodea kortxetez inguratutako blokez `[...]` osatuta dago eta bloke bakoitza PIN-aren digitu bati dagokio.

Bloke arrunt batek `[nOP...]` itxura du, non `n` zenbaki bat (0-9) baita eta ondoren eragiketa matematikoen (hautazko) zerrenda bat egon daitekeen.

Eragiketak ordenan aplikatzen zaizkio zenbakiari eta honakoak izan daitezke:

- `+` 1 gehitzen du
- `-` 1 kentzen du

Emaitza beti da digitu bat (mod 10 aritmetika), adibidez `9 + 1 → 0` eta `0 - 1 → 9`.

Honetaz gain, bloke berezi bat `[<]` ere badago, aurreko blokeko zenbakia errepikatzen duena.

Amaieran 4 digitu baino gutxiago badaude, `null` itzuli behar da.


## 💡 Adibideak

```js
decodeSantaPin('[1++][2-][3+][<]')
// "3144"

decodeSantaPin('[9+][0-][4][<]')
// "0944"

decodeSantaPin('[1+][2-]')
// null (2 digitu bakarrik)
```