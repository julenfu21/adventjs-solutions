<div align="center">
    <h1>Erronka #13: 🏭 Muntaketa-Katea</h1>
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

Opariak lantegian zehar egingo duen bidea simulatu eta amaierako egoera itzuli. Hau egiteko, `runFactory(factory)` funtzio bat sortu behar duzu.

`factory` `string[]` bat da eta elementu bakoitzak honako balioak har ditzake:

- `>` `<` `^` `v` mugimenduak
- `.` irteera zuzena

Kontuan izan **errenkada guztiek luzera berdina izango dutela** eta **aipatutako sinboloetaz gain, ez da beste sinbolo desberdinik agertuko**.

Opariaren **abiapuntua beti (0, 0) posizioa izango da** (goian ezkerrean). Pauso bakoitzean uneko posizioari dagokion elementua irakurtzen da eta oparia zehaztutako norabidean mugitzen da. Puntu bat (`.`) duen posizio batera iristen bagara, oparia lantegitik atera dela esan nahi du.

**Emaitza**

Balio hauetatik bat itzuli:

- `'completed'` puntu batera `.` iristen bada
- `'loop'` posizio batetik behin baino gehiagotan igarotzen bada
- `'broken'` taulatik ateratzen bada


## 💡 Adibideak

```js
runFactory([
  '>>.'
]) // 'completed'

runFactory([
  '>>>'
]) // 'broken'

runFactory([
  '>><'
]) // 'loop'

runFactory([
  '>>v',
  '..<'
]) // 'completed'

runFactory([
  '>>v',
  '<<<'
]) // 'broken'

runFactory([
  '>v.',
  '^..'
]) // 'completed'

runFactory([
  'v.',
  '^.'
]) // 'loop'
```