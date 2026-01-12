<div align="center">
    <h1>Erronka #17: 🎄 Gabonetako Argien Panela</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Zailtasuna-ERRAZA-brightgreen" alt="Zailtasuna: Erraza">
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Ipar poloan, **gabonetako argien panel bat** 🎄✨ jarri dute lantegia apaintzeko. Argi bakoitzak kolore batekin piztuta egon daiteke edo itzalita.

Panela **matrize** baten bidez adierazita dago eta gelaxka bakoitzak honako balioak har ditzake:

- `'.'` → argi itzalia
- `'R'` → argi gorria
- `'G'` → argi berdea

Iratxoek ea **kolore bereko 4 argiz osatutako lerroren bat** dagoen jakin nahi dute (soilik horizontal ↔ eta bertikal ↕ norabideetan). Itzalita dauden argiek (`'.'`) ez dute balio.


## 💡 Adibideak

```js
hasFourLights([
  ['.', '.', '.', '.', '.'],
  ['R', 'R', 'R', 'R', '.'],
  ['G', 'G', '.', '.', '.']
])
// true → 4 argi gorrik lerro horizontal bat osatzen dute

hasFourLights([
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.']
])
// true → 4 argi berdek lerro bertikal bat osatzen dute

hasFourLights([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → ez dago kolore bereko 4 argiz osatutako lerrorik
```

**Oharra:** Taularen tamaina edozein izan daiteke. Ez dago diagonalik.