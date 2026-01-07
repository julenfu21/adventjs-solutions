<div align="center">
    <h1>Erronka #8: 🎁 Jostailu Bakana Aurkitu</h1>
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

Bizarzurik 🎅 opari baten izenean 🎁 errepikatzen ez den lehenengo hizkia zein den jakin nahi du.

Idatz ezazu sarrera-parametro gisa `string` bat hartzen eta errepikatzen ez den lehenengo hizkia itzultzen duen funtzio bat. Hizki larri eta xeheak berdinak izango balira bezala hartzen dira, baina itzultzen den hizkia string-ean agertzen den bezala itzuli behar da.

Errepikatzen ez den hizkirik ez badago, string hutsa itzuli ("").


## 💡 Adibideak

```js
findUniqueToy('Gift') // 'G'
// ℹ️ G errepikatzen ez den lehenengo hizkia da
// eta agertzen den moduan itzultzen da

findUniqueToy('sS') // ''
// ℹ️ Hizkiak errepikatuta daude, hizki larri eta xeheak ez baitira bereizten

findUniqueToy('reindeeR') // 'i'
// ℹ️ r hizkia errepikatuta dago (nahiz eta bat 
// larria eta bestea xehea izan) eta e hizkia ere
// errepikatuta dago. Beraz, lehenengo hizkia 'i' da.

// Kasu gehiago:
findUniqueToy('AaBbCc') // ''
findUniqueToy('abcDEF') // 'a'
findUniqueToy('aAaAaAF') // 'F'
findUniqueToy('sTreSS') // 'T'
findUniqueToy('z') // 'z'
```