<div align="center">
    <h1>Erronka #7: 🎄 Zuhaitza Apaintzen</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuazioa-7%2F8-blueviolet" alt="Puntuazioa: 7-8" style="vertical-align: middle;"> | [Inplementaziora Joan](python/README.eu.md) |


## 🎯 Argibideak

**Gabonetako zuhaitza** 🎄 apaintzeko ordua heldu da! Sarrera-parametro gisa honakoa jasotzen duen funtzio bat idatz ezazu:

- `height` → zuhaitzaren altuera (lerro kopurua).
- `ornament` → apaingarri gisa erabilitako karakterea (adibidez, `"o"` edo `"@"`).
- `frequency` → zenbat posiziotan behin agertzen den apaingarria.

Zuhaitza izartxoekin `*` marrazten da, baina **`frequency` posiziotan behin**, izartxoa apaingarriagatik ordezkatzen da.

Posizioak 1etik kontatzen hasten dira, goitik behera eta ezkerretik eskuinera. `frequency` 2 bada, apaingarriak hurrengo posizioetan agertuko dira: 2, 4, 6, etab.

Zuhaitza erdian kokatuta agertu behar da eta amaieran lerro bakarreko enborra `#` izan behar du. **Kontuz zuriuneekin, inoiz ez dago zuriunerik lerro bakoitzaren amaieran.**


## 💡 Adibideak

```js
drawTree(5, 'o', 2)
//     *
//    o*o
//   *o*o*
//  o*o*o*o
// *o*o*o*o*
//     #

drawTree(3, '@', 3)
//   *
//  *@*
// *@**@
//   #

drawTree(4, '+', 1)
//    +
//   +++
//  +++++
// +++++++
//    #
```