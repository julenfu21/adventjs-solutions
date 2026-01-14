<div align="center">
    <h1>Erronka #22: 🎄 Leraren Labirintoa — Python</h1>
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

Karpeta honek Erronka #22ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #22ren README nagusira](../README.eu.md).


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
# <test_funtzioa> = {test_can_escape_returns_boolean, test_can_escape}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 8}

pytest test_solution.py::test_can_escape[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak Breadth-First Search (BFS) algoritmoa era egokian inplementatzen du.
- Funtzio laguntzaileak ondo definitu dira eta irakurgarritasuna hobetzen dute.
- `dataclass` baten erabilera aproposa da posizioaren koordenatuak `Square` klasearen bidez adierazteko.
- Abiapunturik ez dagoen salbuespen-kasua era egokian kudeatu da `ValueError` baten bitartez.
- Inplementatutako BFS algoritmoaren logikak *ilara* eta *sorta* datu-egiturak era egokian erabiltzen ditu bisitatutako gelaxkak kudeatzeko.


### ⚠️ Ahuleziak

- `get_start_position` funtzioak labirinto osoa iteratzen du, nahiz eta 'S' lehenago aurkitu izan. Prozesu hau 'S' aurkitu bezain laster balio hori itzultzen optimiza liteke.
- `are_valid_coordinates` funtzioak `maze[row][column] != '#'` konprobaketa egiten du, baina ez da beharrezkoa dagoeneko `get_square_neighbors` funtzioak egiten baitu koordenatuak bizilagunen zerrendan sartu baino lehen. Konprobaketa hau gelaxka bizilagunak aztertzen diren momentura mugi liteke.


### 🧭 Hurrengo Pausoak

- `get_start_position` funtzioa optimizatu, 'S' balioa aurkitu bezain laster, balio hori itzuli eta funtzioa amaitzeko.
- `are_valid_coordinates` funtzioan mugen konprobaketa egiten den lekua aztertu; baliteke konprobaketa hori beharrezkoa ez izatea.