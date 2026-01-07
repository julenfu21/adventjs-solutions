<div align="center">
    <h1>Erronka #6: 🧤 Eskularruak Parekatzen — Python</h1>
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

Karpeta honek Erronka #6ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #6ren README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ERRAZA-brightgreen" alt="Zailtasuna: Erraza" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Testak

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_match_gloves_returns_list, test_match_gloves}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 9}

pytest test_solution.py::test_match_gloves[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak kolore bereko ezkerreko eta eskuineko eskularruak era egokian identifikatzen ditu.
- `defaultdict` era eraginkorrean erabiltzen da eskularruen kopurua gordetzeko.
- Bikoteak osatzeko eta amaierako zerrenda osatzeko logika zentzuzkoa da.
- Eskatu den moduan, funtzioak zerrenda hutsa itzultzen du bikoterik osatu ez bada.
- Kodeak Python-en praktika onak jarraitzen ditu, aldagaientzako izen argiak eta formatu egokia erabilita.