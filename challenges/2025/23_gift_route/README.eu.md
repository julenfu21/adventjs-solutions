<div align="center">
    <h1>Erronka #23: 🎁 Oparien Ibilbidea</h1>
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

Bizarzurik 🎅 opariak banatu behar ditu herrian zehar, **lauki-sare baten bidez adierazitako mapa batean**.

Mapako gelaxka bakoitzak honako balioak har ditzake:

- `'S'` → Bizarzuriren abiapuntua (opariak hemen daude)
- `'G'` → Opariak jaso behar dituen etxea
- `'.'` → Oztoporik gabeko bidea
- `'#'` → Oztopoa (ezin de zeharkatu)

Bizarzurik bidaia desberdinak egiten ditu opari bakoitzeko. `'S'` posiziotik abiatzen da, oparia `'G'` posizioan uzten du eta **berehala `'S'` posiziora itzultzen da** hurrengo oparia hartzeko. Hala ere, erronka honetarako, `'S'` posiziotik `'G'` etxe bakoitzaren posiziora arte **noranzko bakarrean egin beharreko distantzia minimoen batura baino ez dugu kalkulatu nahi**.


## 🏁 Helburua

`minStepsToDeliver(map)` funtzioa idatz ezazu. Funtzio honek opariak etxe guztietan banatzeko egin beharreko **pauso kopuru totala** itzultzen du.

Honakoa kontuan izan:

- Ibilbidea beti `'S'` posiziotik hasiko da.
- Opari bakoitzeko, `'S'` posiziotik dagokion `'G'` posiziora iristeko egin beharreko **distantzia minimoa** kalkulatu behar duzu.
- Oztopoak (`'#'`) ezin dira zeharkatu.
- Etxeren batera iristea ezinezkoa bada, funtzioak `-1` itzuli behar du.


## 💡 Adibideak

```js
minStepsToDeliver([
  ['S', '.', 'G'],
  ['.', '#', '.'],
  ['G', '.', '.']
])
// Emaitza: 4

/* 
Azalpena:
- S (0,0) posiziotik G (0,2) posiziora iristeko distantzia minimoa: 2 pauso
- S (0,0) posiziotik G (2,0) posiziora iristeko distantzia minimoa: 2 pauso
- Distantzia totala: 2 + 2 = 4
*/

minStepsToDeliver([
  ['S', '#', 'G'],
  ['#', '#', '.'],
  ['G', '.', '.']
])
// Emaitza: -1
// ((0,2) posizioan dagoen etxera heltzea ezinezkoa da oztopoak direla eta)

minStepsToDeliver([['S', 'G']])
// Emaitza: 1
```


## 📜 Arauak

- Mapak zehazki `'S'` bakar bat izango du beti.
- Zero edo etxe gehiago egon daitezke opariak banatzeko (`'G'`).
- Opariak banatzeko ordenak ez du garrantzirik, bide bakoitzeko distantzia modu independentean neurtzen baita, `'S'` posiziotik abiatuta.
- **Noranzko bakarrean egin beharreko distantzia minimoen batura** itzuli behar duzu. 


## 🧠 Aholkuak

- `'S'` posiziotik `'G'` posizio bakoitzera dagoen distantzia laburrena kalkulatu (horretarako Breadth-First Search edo BFS algoritmoa erabil dezakezu).
- Opariren bat banatzea ezinezkoa bada, emaitza totala `-1` izan behar da.