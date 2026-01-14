<div align="center">
    <h1>Erronka #24: 🪞 Egiaztatu ea Zuhaitzak Ispilu Magikoak Diren — Python</h1>
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

Karpeta honek Erronka #24ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #24ren README nagusira](../README.eu.md).


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
# <test_funtzioa> = {test_is_trees_synchronized_returns_list, test_is_trees_synchronized}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 7}

pytest test_solution.py::test_is_trees_synchronized[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak bi zuhaitz bitar ea bata bestearen ispilua den egiaztatzeko logika era egokian inplementatzen du.
- `are_trees_equal` funtzioan errekurtsibitatearen erabilera aproposa da zuhaitzak zeharkatzeko.
- `get_subtree_or_none` funtzio laguntzaileak irakurgarritasuna hobetzen du hiztegiaren erabilera ezkutatzen duen abstrakzio maila bat erantsita.
- Kodeak zuhaitz hutsak bezalako salbuespen-kasuak era egokian kudeatzen ditu.
- Amaierako return adierazpenak bi zuhaitzen sinkroniaren eta lehenengo zuhaitzaren erroaren balioaren berri era egokian ematen du.