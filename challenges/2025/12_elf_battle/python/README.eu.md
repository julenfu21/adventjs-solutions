<div align="center">
    <h1>Erronka #12: ⚔️ Iratxoen Borroka — Python</h1>
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

Karpeta honek Erronka #12ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #12ren README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ERTAINA-yellow" alt="Zailtasuna: Ertaina" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-6%2F8-lightcoral" alt="Puntuazioa: 5-6" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Testak

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_elf_battle_returns_int, test_elf_battle}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 8}

pytest test_solution.py::test_elf_battle[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak borrokaren logika era egokian inplementatzen du eta iratxo bakoitzaren mugimenduak aldi berean kudeatzen ditu.
- `attack_other_player` eta `has_player_lost` funtzio laguntzaileek irakurgarritasuna hobetzen dute.
- Bi iratxoek aldi berean galtzea eta borroka bat txanda guztiak aztertu baino lehen amaitzea bezalako salbuespen-kasuak ondo kudeatu dira.


### ⚠️ Ahuleziak

- Konplexutasun ziklomatikoa altua da, hala begizta nagusian nola funtzio laguntzaileetan erabilitako habiaratutako baldintzen logika dela eta.


### 🧭 Hurrengo Pausoak

- `attack_other_player` funtzioaren baldintzen logika berridaztea gomendatzen da habiaraketa-maila murrizteko eta argitasuna hobetzeko. Adibidez, `if/elif/else` baldintzazko adierazpenen segida bat erabiltzea hainbat `if` independente erabiltzea baino zuzenagoa izan liteke.