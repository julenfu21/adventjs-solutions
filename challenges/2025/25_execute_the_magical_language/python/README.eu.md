<div align="center">
    <h1>Erronka #25: 🪄 Hizkuntza Magikoa Egikaritu — Python</h1>
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

Karpeta honek Erronka #25eko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #25en README nagusira](../README.eu.md).


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
# <test_funtzioa> = {test_execute_returns_int, test_execute}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 13}

pytest test_solution.py::test_execute[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Kodeak sarrera-parametro gisa jasotako string-a lantzeko erabiltzen duen logika egokia da.
- Begiztak eta baldintzak prozesatzeko erabilitako funtzio laguntzaileek irakurgarritasuna hobetzen dute.
- Kodeak erronkaren enuntziatuan deskribatutako egitura habiaratuak era egokian kudeatzen ditu.


### ⚠️ Ahuleziak

- `get_scope_of_special_expression` funtzioak errore potentzial bat du: `expression_end_symbol` beti aurkituko dela ziurtzat hartzen du eta simboloa ez dagoen kasua ez da aztertzen.
- `process_loop_expression` funtzioa begizta infinitu batean sar liteke `current_value` aldagaiak begiztaren barruan 0 balioa inoiz ez badu hartzen, ez baitu begiztatik ateratzeko erarik `current_value` aldagaiak 0 balioa hartu gabe.


### 🧭 Hurrengo Pausoak

- `get_scope_of_special_expression` funtzioan amaierako sinboloaren faltak sortuko lukeen errorea landu.
- `process_loop_expression` funtzioan iterazio kopuru maximo bat jarri babes mekanismo modura, begizta infinitu potentzialak ekiditeko, nahiz eta erronkaren enuntziatuan sarrera-parametro egokiak soilik agertu.