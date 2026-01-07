<div align="center">
    <h1>Erronka #5: ⏱️ Aireratzerako Atzerako Kontaketa — Python</h1>
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

Karpeta honek Erronka #5eko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #5en README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ERRAZA-brightgreen" alt="Zailtasuna: Erraza" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Tests

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_time_until_take_off_returns_int, test_time_until_take_off}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 8}

pytest test_solution.py::test_time_until_take_off[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak erronkako data formatu berezia era egokian analizatu eta denboren arteko aldea segundotan kalkulatzen du.
- Aireratze-unean bertan gauden edo aireratzea dagoeneko gertatu den salbuespen-kasuak ondo kudeatzen dira.
- `datetime.strptime` eta `total_seconds` funtzioen erabilera egokia eta eraginkorra da.


### 🧭 Hurrengo Pausoak

- `north_pole_format` aldagaia konstante bat bezala definitu liteke kodearen irakurgarritasuna eta mantenigarritasuna hobetzeko, formatu hau beste nonbait erabili beharko balitz bereziki.