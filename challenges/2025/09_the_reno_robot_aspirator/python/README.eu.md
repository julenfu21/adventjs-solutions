<div align="center">
    <h1>Erronka #9: 🦌 Elur-Orein Xurgagailua — Python</h1>
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

Karpeta honek Erronka #9ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #9ren README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ZAILA-red" alt="Zailtasuna: Zaila" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Testak

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_move_reno_returns_string, test_move_reno}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 9}

pytest test_solution.py::test_move_reno[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak era egokian aurkitzen du elur-oreinaren hasierako posizioa.
- Elur-oreinaren mugimendua zehastasunez simulatzen da sarrera-parametro gisa jasotako balioen arabera.
- Taulatik atzeratzen edo oztopo batekin talka egiten den salbuespen-kasuak ondo kudeatzen dira.
- Zorutik zerbait jasotzen denean 'success' itzultzeko aplikatzen den logika zentzuzkoa da.
- Kodea ondo egituratuta dago eta irakurterraza da.


### ⚠️ Ahuleziak

- Konplexutasun ziklomatikoa apur bat handia da (14). Hau baldintzen logika berridatzita hobe liteke.


### 🧭 Hurrengo Pausoak

- Mugimenduen eta mugen/oztopoen egiaztapenerako logika berridaztea gomendatzen da konplexutasun ziklomatikoa txikiagotzeko. Adibidez, funtzio laguntzaile bat mugimendu bakoitzaren ostean egungo egoera aztertzeaz ardura daiteke.