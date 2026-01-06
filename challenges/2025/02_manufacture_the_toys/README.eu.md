<div align="center">
    <h1>Erronka #2: 🏭 Jostailuak Ekoiztu</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-6%2F8-lightcoral" alt="Puntuazioa: 5-6" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Bizarzuriren lantegia **ekoiztu beharreko jostailuen zerrenda** jasotzen hasi da. Lerro bakoitzak zein jostailu eta zenbat ale ekoiztu behar diren adierazten du.

Iratxoek, beti bezala, hanka sartu dute: jostailu batzuk zentzurik ez duten kopuruekin idatzi dituzte.

Honako egitura duen zerrenda bat duzu:

- `toy`: jostailuaren izena (string)
- `quantity`: ekoiztu beharreko ale kopurua (number)

Zure eginkizuna sarrera-parametro gisa zerrenda hau hartzen duen eta honako baldintzak betetzen dituen **string-ez osatutako array bat** itzultzen duen funtzio bat idaztea da:

- Jostailu bakoitza `quantity` aldiz errepikatuta egon behar da.
- Jostailuek jatorrizko zerrendako ordena mantendu behar dute.
- Ale kopuru baliogabea duten jostailuak (0 edo txikiagoa, edo zenbakia ez den balioa) baztertu egin behar dira.


## 💡 Adibideak

```js
const production1 = [
  { toy: 'car', quantity: 3 },
  { toy: 'doll', quantity: 1 },
  { toy: 'ball', quantity: 2 }
]

const result1 = manufactureGifts(production1)
console.log(result1)
// ['car', 'car', 'car', 'doll', 'ball', 'ball']

const production2 = [
  { toy: 'train', quantity: 0 }, // hau ez da ekoizten
  { toy: 'bear', quantity: -2 }, // ezta hau ere
  { toy: 'puzzle', quantity: 1 }
]

const result2 = manufactureGifts(production2)
console.log(result2)
// ['puzzle']

const production3 = []
const result3 = manufactureGifts(production3)
console.log(result3)
// []
```