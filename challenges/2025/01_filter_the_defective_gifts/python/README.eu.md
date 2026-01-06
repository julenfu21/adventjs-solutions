<div align="center">
    <h1>Erronka #1: 🎁 Opari Akastunak Iragazi — Python</h1>
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

Karpeta honek Erronka #1eko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #1en README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ERRAZA-brightgreen" alt="Zailtasuna: Erraza" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-6%2F8-lightcoral" alt="Puntuazioa: 5-6" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Tests

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_filter_gifts_returns_list, test_filter_gifts}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 6}

pytest test_solution.py::test_filter_gifts[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodea laburra da eta Python-en *"list comprehension"* era eraginkorrean erabiltzen du iragazteko.
- Zerrenda hutsa bezalako salbuespen-kasuak era egokian kudeatzen ditu.
- Logika zuzena eta ulerterraza da.