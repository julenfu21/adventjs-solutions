<div align="center">
    <h1>Erronka #4: 🧮 Bizarzuriren PIN-a Deszifratu — Python</h1>
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

Karpeta honek Erronka #4ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #4ren README nagusira](../README.eu.md).


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
# <test_funtzioa> = {test_decode_santa_pin_returns_string, test_decode_santa_pin}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 8}

pytest test_solution.py::test_decode_santa_pin[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak sarrera-parametro gisa jasotako string-a era egokian analizatu eta PIN-a deszifratzen du.
- `process_block` funtzio laguntzailea ondo definituta dago eta eragiketa ondo kudeatzen ditu.
- Mod 10 aritmetika era egokian inplementatu da.
- 4 digitu baino gutxiago dituen salbuespen-kasua ondo kudeatu da `null` balioa itzulita.
- Aldagaien izenak orokorrean deskribatzaileak dira.


### ⚠️ Ahuleziak

- `process_block` funtzioak `ValueError` salbuespena botatzen du '<' eragiketarako `last_digit` `None` denean. Programa nagusiak ez du salbuespen hau antzematen. Ondorioz, kodea '[<]' blokearekin hasten bada kodea errore bat bota dezake.
- Begizta nagusiak kodea karakterez karaktere iteratzen du. Hau ez da espresio erregularrak erabiltzea edo string-a zatitzea gero blokeak identifikatzeko baino eraginkorragoa.


### 🧭 Hurrengo Pausoak

- Errore kudeaketa mekanismo bat gehitu `process_block` funtzio barruko `ValueError` salbuespena antzemateko eta `None` edo adierazle apropos bat baldin eta '<' eragiketa erabiltzen bada aurretik digiturik agertu gabe.
- Blokeak identifikatzeko logika berridatzi era eraginkorragoan egiteko, besteak beste, blokeak zuzenean erauzteko espresio erregularrak erabilita.