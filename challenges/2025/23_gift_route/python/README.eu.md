<div align="center">
    <h1>Erronka #23: 🎁 Oparien Ibilbidea — Python</h1>
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

Karpeta honek Erronka #23ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #23ren README nagusira](../README.eu.md).


## 📊 Erronkaren Xehetasunak

| Zailtasun Maila | Puntuazioa |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Zailtasuna-ERTAINA-yellow" alt="Zailtasuna: Ertaina" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> |


## 💻 Ebazpena

Begiratu [`solution.py`](solution.py) inplementazioa ikusteko.


## 🧪 Testak

Test guztiak egikaritu:

```bash
pytest test_solution.py
```

Test-funtzio jakin bat egikaritu:

```bash
# <test_funtzioa> = {test_min_steps_to_deliver_returns_int, test_min_steps_to_deliver}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 6}

pytest test_solution.py::test_min_steps_to_deliver[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak BFS algoritmoa ondo inplementatzen du biderik laburrena topatzeko.
- Funtzio laguntzaileak ondo definitu dira eta irakurgarritasuna hobetzen dute.
- Iristea ezinezkoa diren etxeak bezalako salbuespen-kasuak era egokian kudeatu dira.


### ⚠️ Ahuleziak

- BFS algoritmoaren inplementazioa ez da guztiz optimoa aldi berean hainbat etxetara distantzia laburrenak era eraginkorrean topatzeko. 'S' posiziotik hasita, igaro daitekeen posizio guztiak aztertzen dira eta ondoren ea etxe guztiak bisitatu diren begiratzen da. Hori egin beharrean, hobeto izango litzateke etxe bakoitzeko BFS algoritmoa exekutatzea edo aldi berean hainbat etxetara bideratutako BFS algoritmoaren exekuzio bat egitea.
- `remaining_houses` aldagaiaren logika ez da guztiz zuzena. `remaining_houses` balioari 1 kentzen zaio etxeren bat aurkitzen bada, baina `while queue and remaining_houses >= 0:` baldintzak ez du etxe guztiak bisitatu direla bermatzen, *ilara* datu-egitura etxe guztiak bisitatu baino lehen husten bada. Proposamen hobeago bat, etxe bakoitzaren egoera aldagai batean gordetzea eta prozesu amaieran ea guztiak bisitatu diren egiaztatzea izan liteke.


### 🧭 Hurrengo Pausoak

- BFS algoritmoa berridatzi 'G' posizio guztietarako dauden distantziak era eraginkorrean kalkulatzeko. 'S' posiziotik 'G' posizio bakoitzera BFS algoritmoaren exekuzio desberdin bat egin liteke. Beste aukera bat, aurkitzen diren 'G' guztietarako distantziak gordetzen dituen BFS exekuzio bakarra egitea da.
- Momentu bakoitzean aurkitutako etxeak kontrolatzeko erabili den logika moldatu, -1 balioa itzuli baino lehen etxe guztiak bisitatu direla egiaztatzeko.