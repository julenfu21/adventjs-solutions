<div align="center">
    <h1>Erronka #7: 🎄 Zuhaitza Apaintzen — Python</h1>
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

Karpeta honek Erronka #7ko **ebazpena eta testak** ditu, <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**-ekin osatutakoak. Erronkaren azalpen zehaztuagoa ikusteko jo [Erronka #7ren README nagusira](../README.eu.md).


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
# <test_funtzioa> = {test_draw_tree_returns_string, test_draw_tree}

pytest test_solution.py::<test_funtzioa>
```

Parametrizatutako test-kasu jakin bat egikaritu:

```bash
# <indizea> = {2 - 6}

pytest test_solution.py::test_draw_tree[test-<indizea>]
```


## 🧠 Kodearen Azterketa


### ✅ Sendotasunak

- Apaingarriak dagokien tokian kokatzeko logika era egokian inplementatu da.
- Zuhaitza erdian kokatu da eta amaieran lerro bakarreko enborra erantsi zaio.
- Kodea garbia, irakurterraza eta *"Pythonikoa"* da.
- Aldagaientzako izen deskribatzaileak erabiltzen dira.


### 🧭 Hurrengo Pausoak

- `TREE_ELEMENT`, `WHITESPACE`, eta `TRUNK_ELEMENT` funtziotik kanpo konstante bezala definitzea gomendagarria izango litzateke beste leku batean berrerabili beharko balira. Hala ere, funtzio batean soilik erabiltzekotan, aldagai hauen kokalekua onargarria da. 