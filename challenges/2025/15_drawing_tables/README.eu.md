<div align="center">
    <h1>Erronka #15: ✏️ Taulak Marrazten</h1>
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

**ChatGPT Ipar Polora heldu da** eta *Sam Elfman* iratxoa umeen eta oparien kudeaketarako aplikazio batean lan egiten ari da.

Honen itxura hobetzeko `drawTable` funtzio bat sortu nahi du, sarrera-parametro gisa **objektuen array bat** jaso eta **testu-taula** batean bihurtzen duena.

Marraztutako taulak honako baldintzak bete behar ditu:

- Zutabe bakoitzean hizki bat (`A`, `B`, `C`…) duen goiburua.
- Taularen edukia objektuen balioekin osatuko da.
- Balioak ezker-lerrokatuak izan behar dira.
- Eremu bakoitzak zuriune bat izango du ezkerraldean.
- Eremu bakoitzak eskuinean behar bezainbeste zuriune izango ditu zutabe osoan zehar zabalera bera mantentzeko.

Funtzioak bigarren `sortBy` sarrera-parametro bat jasotzen du, errenkadak zein zutaberen arabera ordenatu behar diren zehazten duena. Balioak txikienetik handienera eta alfabeto-ordena mantenduta ordenatuko dira.

Azter ezazu beheko adibidea marraztu beharreko taulak zer itxura izan beharko lukeen ikusteko: 


## 💡 Adibideak

```js
drawTable(
  [
    { name: 'Charlie', city: 'New York' },
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' }
  ],
  'name'
)
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

drawTable(
  [
    { gift: 'Book', quantity: 5 },
    { gift: 'Music CD', quantity: 1 },
    { gift: 'Doll', quantity: 10 }
  ],
  'quantity'
)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
```