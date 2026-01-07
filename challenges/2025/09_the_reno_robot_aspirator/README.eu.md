<div align="center">
    <h1>Erronka #9: 🦌 Elur-Orein Xurgagailua</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Zailtasuna-ZAILA-red" alt="Zailtasuna: Zaila">
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

Iratxoek **🦌 elur-orein xurgagailu** (`@`) bat eraiki dute gabonetara begira lantegia apur bat garbitzeko.

Elur-oreina taula batean zehar mugitzen da **zorutik gauzak jasotzeko** (`*`) eta **oztopoak saihestu** (`#`) behar ditu.

Bi sarrera-parametro jasoko dituzu:

- `board`: taula irudikatzen duen `string` bat.
- `moves`: mugimenduak dituen `string` bat: `'L'` (ezkerrera), `'R'` (eskuinera), `'U'` (gora), `'D'` (behera).

**Mugimenduen arauak**:

- Elur-oreinak mugimenduetan zehar **zorutik zerbait jasotzen badu** (`*`) → `'success'` itzuli.
- Elur-oreina **taulatik ateratzen bada** edo honek **oztopo batekin talka egiten badu** (`#`) → `'crash'` itzuli.
- Elur-oreinak **ez badu ezer ez jasotzen ezta talka egin ere** → `'fail'` itzuli.

Kontuan izan elur-oreinak **zorutik zerbait jasotzen badu**, dagoeneko `'success'` itzuli behar dela, nahiz eta hurrengo mugimenduetan oztopo batekin talka egin edo taulatik atera.

**Garrantzitsua**: Aintzat hartu `board` aldagaian lehenengo eta azken ilarak hutsik daudela, eta ondorioz baztertu egin behar direla.


## 💡 Adibideak

```js
const board = `
.....
.*#.*
.@...
.....
`

moveReno(board, 'D')
// ➞ 'fail' -> mugitu egiten da baina ez du ezer ez jasotzen

moveReno(board, 'U')
// ➞ 'success' -> zerbait jasotzen du (*) goian hain zuzen ere

moveReno(board, 'RU')
// ➞ 'crash' -> oztopo batekin talka egiten du (#)

moveReno(board, 'RRRUU')
// ➞ 'success' -> zerbait jasotzen du (*)

moveReno(board, 'DD')
// ➞ 'crash' -> taularen beheko aldearekin talka egiten du

moveReno(board, 'UUU')
// ➞ 'success' -> zerbait jasotzen du (*) eta gero taularen goiko aldearekin talka egiten du

moveReno(board, 'RR')
// ➞ 'fail' -> mugitu egiten da baina ez du ezer ez jasotzen
```