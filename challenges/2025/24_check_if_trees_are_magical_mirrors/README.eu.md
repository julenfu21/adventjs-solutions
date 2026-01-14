<div align="center">
    <h1>Erronka #24: 🪞 Egiaztatu ea Zuhaitzak Ispilu Magikoak Diren</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-8%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

Ipar poloan, iratxoek **energia sortzen duten bi zuhaitz bitar magiko** 🌲🌲 dituzte gabonetako izarrak ⭐️ bere distira manten dezan. Alabaina, ondo funtziona dezaten, zuhaitzak guztiz sinkronizatuta egon behar dira, **bata bestearen ispilu baten islada izango balitz bezala** 🪞.

**Bi zuhaitz bitar ispiluak izango dira baldin eta:**

- Bi zuhaitzen erroek balio bera badute.
- Lehenengo zuhaitzaren nodo bakoitzak dagokion nodoa izan behar du, bigarren zuhaitzak nodo bera duen aurkako posizioan.

Zuhaitz bakoitza `value`, `left` eta `right` hiru balioen bitartez adierazita dago. Gainera, azken bi balioek gainontzeko adarrei dagozkien balioak dituzte.

```js
const tree = {
  value: '⭐️',
  left: {
    value: '🎅'
    // left: {...}
    // right: { ... }
  },
  right: {
    value: '🎁'
    // left: { ... }
    // right: { ...&nbsp;}
  }
}
```

Bizarzurik zure laguntza behar du zuhaitzak ea sinkronizatuta dauden egiaztatzeko, eta ondorioz gabonetako izarrak bere distira manten dezan. **Array bat itzuli behar duzu**, non **lehenengo posizioak ea zuhaitzak sinkronizatuta dauden** eta **bigarren posizioak lehenengo zuhaitzaren erroak duen balioa** adierazten duen.


## 💡 Adibideak

```js
const tree1 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

const tree2 = {
  value: '🎄',
  left: { value: '🎅' }
  right: { value: '⭐' },
}

isTreesSynchronized(tree1, tree2) // [true, '🎄']

/*
  tree1          tree2
   🎄              🎄
  / \             / \
⭐   🎅         🎅   ⭐
*/

const tree3 = {
  value: '🎄',
  left: { value: '🎅' },
  right: { value: '🎁' }
}

isTreesSynchronized(tree1, tree3) // [false, '🎄']

const tree4 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

isTreesSynchronized(tree1, tree4) // [false, '🎄']

isTreesSynchronized(
  { value: '🎅' },
  { value: '🧑‍🎄' }
) // [false, '🎅']
```