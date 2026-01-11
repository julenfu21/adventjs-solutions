<div align="center">
    <h1>Erronka #14: 🗃️ Oparirako Bidea Aurkitu</h1>
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

Ipar Poloan, iratxoek opariak biltegiratzeko sistema sinplifikatu dute akatsak ekiditeko. Orain opariak **sakonera-maila mugatua duten objektu magikoen** barruan gordetzen dituzte, non **balio bakoitza behin bakarrik agertzen baita**.

Bizarzurik era azkar bat behar du opari jakin bat topatzeko **gakoen zein bide** jarraitu behar duen jakiteko.

Zure egitekoa sarrera-parametro gisa objektu bat eta balio bat hartzen dituen funtzio bat idaztea da, oparia topatzeko jarraitu beharreko **gakoen array bat** itzultzen duena.

**Arauak:**

- Objektuaren **gehienezko sakonera-maila 3 izango da**.
- Aurkitu beharreko balioa **geheienez behin agertuko da**.
- Objektu bakoitzak **beste objektu bat edo balio primitibo bat** (strings, numbers, booleans) izango du balio gisa.
- Balioa aurkitzen ez bada, array hutsa itzuli behar da.


## 💡 Adibideak

```js
const workshop = {
  storage: {
    shelf: {
      box1: 'train',
      box2: 'switch'
    },
    box: 'car'
  },
  gift: 'doll'
}

findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']

findGiftPath(workshop, 'switch')
// ➜ ['storage', 'shelf', 'box2']

findGiftPath(workshop, 'car')
// ➜ ['storage', 'box']

findGiftPath(workshop, 'doll')
// ➜ ['gift']

findGiftPath(workshop, 'plane')
// ➜ []
```