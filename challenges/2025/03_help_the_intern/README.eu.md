<div align="center">
    <h1>Erronka #3: 👶 Praktiketako Langileari Lagundu</h1>
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

Bizarzuriren lantegian praktiketako iratxo bat dago opariak biltzen ikasten ari dena 🎁.

Iratxoari kutxak testua soilik erabiliz biltzea eskatu diote… eta *gutxi gorabehera* egiten du.

Bi sarrera-parametro jasotzen ditu:

- `size`: opari karratuaren tamaina
- `symbol`: iratxoak ertza egiteko erabiltzen duen karakterea (okertzen ez denean 😅)

Opariak honako baldintza hauek bete behar ditu:

- `size x size` tamainako **karratua** izan behar da.
- Barrualdea beti hutsik dago (zuriunez betea), iratxoak oraindik ez dakielako "barrualdea marrazten".
- `size < 2` bada, string hutsa itzuli behar da: iratxoak ahalaegina egin du, baina oparia galdu egin zaio.
- Azken emaitza string bat izan behar da, lerro-jauziak `\n` dituena.

Bai, erronka erraza da… baina ez dugu praktiketako langilea kaleratzerik nahi, ezta?


## 💡 Adibideak

```js
const g1 = drawGift(4, '*')
console.log(g1)
/*
 ****
 *  *
 *  *
 ****
 */

const g2 = drawGift(3, '#')
console.log(g2)
/*
###
# #
###
*/

const g3 = drawGift(2, '-')
console.log(g3)
/*
--
--
*/

const g4 = drawGift(1, '+')
console.log(g4)
// ""  praktiketako langile gizajoa…
```