<div align="center">
    <h1>Erronka #10: 📨 Gabonetako Magiaren Sakonera — Python</h1>
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

Karpeta honek Erronka #10eko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #10en README nagusira](../README.eu.md).


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
# <test_funtzioa> = {test_max_depth_returns_int, test_max_depth}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 11}

pytest test_solution.py::test_max_depth[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

-  Kodeak kortxeteen proportzioaren oreka era egokian kudeatzen du salbuespen-kasuetan.
- Uneko eta sakonera maila maximoa uneoro kontuan hartzeko logika argi eta eraginkorra da.
- Aldagaiek izen deskribatzaileak dituzte eta kodea *"Pythonikoa"* da.
- Algoritmoa optimoa da erronka honetarako, string-a behin bakarrik zeharkatuz.