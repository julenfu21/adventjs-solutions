<div align="center">
    <h1>Erronka #12: ⚔️ Iratxoen Borroka</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Zailtasuna-ERTAINA-yellow" alt="Zailtasuna: Ertaina">
</p>
<br>


## 🌐 Beste Hizkuntza Batzuetan Irakurri

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Hizkuntza-es-yellow.svg" alt="Gaztelania" style="margin-right:16px;">
    </a>
    <a href="README.md">
        <img src="https://img.shields.io/badge/Hizkuntza-en-red.svg" alt="Ingelesa">
    </a>
</p>


## 💻 Inplementazioak eta Puntuazioak

| Programazio-Lengoaia | Puntuazioa | Inplementazioa |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-6%2F8-lightcoral" alt="Puntuazioa: 5-6" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Bi iratxok txandatan oinarritutako borroka batean dihardute. Bakoitzak `string` baten bidez adierazitako mugimendu sorta bat dauka, non karaktere bakoitza ekintza jakin bati dagokion.

- `A` **Eraso arrunta**: Blokeatzen ez bada, 1 bizitza-puntu kentzen du.
- `B` **Blokeoa**: Eraso arrunt bat (`A`) blokeatzen du.
- `F` **Eraso boteretsua**: 2 bizitza-puntu kentzen ditu eta ezin da blokeatu.

Bi iratxoak **3 bizitza-punturekin** hasten dira. **0 bizitza-puntu edo gutxiagora** heltzen den lehenengo iratxoa izango da galtzailea. Hori gertatu bezain laster borroka amaitu egiten da (hurrengo mugimenduak ez dira kontuan hartzen).

**Txanden arauak**

- Biek eraso bat hautatzen badute (`A` edo `F`), biek bizitza-puntuak galduko dituzte.
- `B` ekintzak `A` ekintza blokeatzen du, baina `F` **ezin du blokeatu**.
- Bi ekintzen ondorioak **aldi berean** ikusiko dira.

**Zure egitekoa**

Borrokaren emaitza adierazten duen zenbaki bat itzul ezazu:

- `1` → Iratxo 1ek irabazten badu
- `2` → Iratxo 2k irabazten badu
- `0` → Berdinketa badago (biak aldi berean 0 bizitza-puntura iristen dira edo bizitza-puntu kopuru berdinarekin bukatzen dute borroka)


## 💡 Adibideak

```js
elfBattle('A', 'B')
// 1. Txanda: A vs B -> Iratxo 2k blokeatu egiten du
// Emaitza: Iratxo 1 = 3 BP
//          Iratxo 2 = 3 BP
// → 0

elfBattle('F', 'B')
// 1. Txanda: F vs B -> Iratxo 2k 2 bizitza-puntu galtzen ditu (F ezin da blokeatu)
// Emaitza: Iratxo 1 = 3 BP
//          Iratxo 2 = 1 BP
// → 1

elfBattle('AAB', 'BBA')
// 1. Txanda: A vs B → Iratxo 2k blokeatu egiten du
// 2. Txanda: A vs B → Iratxo 2k blokeatu egiten du
// 3. Txanda: B vs A → Iratxo 1ek blokeatu egiten du
// Emaitza: Iratxo 1 = 3, Iratxo 2 = 3
// → 0

elfBattle('AFA', 'BBA')
// 1. Txanda: A vs B → Iratxo 2k blokeatu egiten du
// 2. Txanda: F vs B → Iratxo 2k 2 bizitza-puntu galtzen ditu (F ezin da blokeatu)
// 3. Txanda: A vs A → Biek 1 bizitza-puntu galtzen dute
// Emaitza: Iratxo 1 = 2, Iratxo 2 = 0
// → 1

elfBattle('AFAB', 'BBAF')
// 1. Txanda: A vs B → Iratxo 2k blokeatu egiten du
// 2. Txanda: F vs B → Iratxo 2k 2 bizitza-puntu galtzen ditu (F ezin da blokeatu)
// 3. Txanda: A vs A → Biek 1 bizitza-puntu galtzen dute → Iratxo 2 0 bizitza-puntura heltzen da. Borroka amaitu egiten da!
// 4. Txanda: Ez da gehiago borrokatzen, Iratxo 2k bizitza-puntu guztiak galdu baititu.
// → 1

elfBattle('AA', 'FF')
// 1. Txanda: A vs F → Iratxo 1 -2 BP, Iratxo 2 -1 BP
// 2. Txanda: A vs F → Iratxo 1 -2 BP, Iratxo 2 -1 BP → Iratxo 1 -1 BPra heldu da.
// → 2
```