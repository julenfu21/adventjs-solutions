<div align="center">
    <h1>Erronka #18: 🎄 Argiak Lerroan Diagonalekin — Python</h1>
</div>


## 🌐 Beste Hizkuntza Batzuetan Irakurri

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Hizkuntza-es-yellow.svg" alt="Gaztelania" style="margin-right:16px;">
    </a>
    <a href="README.md">
        <img src="https://img.shields.io/badge/Hizkuntza-en-red.svg" alt="Ingelesa">
    </a>
</p>


## 📖 Ikuspegi Orokorra

Karpeta honek Erronka #18ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #18ren README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ERTAINA-yellow" alt="Zailtasuna: Ertaina" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-8%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Testak

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_has_four_in_a_row_returns_boolean, test_has_four_in_a_row}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 6}

pytest test_solution.py::test_has_four_in_a_row[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak kolore bererko 4 argiz osatutako lerro horizontal, bertikal eta diagonalak ondo identifikatzen ditu.
- Funtzio laguntzaileak era egokian definitu dira eta irakurgarritasuna hobetzen dute.
- `all()` eta `any()` funtzioen erabilera egokia da hainbat baldintzen konprobaketarako.
- Taularen mugekin erlazionatutako salbuespen-kasuak era egokian kudeatzen dira funtzio laguntzaileen bidez.