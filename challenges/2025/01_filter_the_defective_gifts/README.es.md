<div align="center">
    <h1>Reto #1: 🎁 Filtrar los Regalos Defectuosos</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-FÁCIL-brightgreen" alt="Dificultad: Fácil">
</p>
<br>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés" style="margin-right:16px;">
    </a>
    <a href="README.eu.md">
        <img src="https://img.shields.io/badge/Idioma-eu-green.svg" alt="Euskera">
    </a>
</p>


## 💻 Implementaciones y Puntuaciones

| Lenguaje | Puntuación | Implementación |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-6%2F8-lightcoral" alt="Puntuación: 5-6" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

Santa ha recibido una lista de regalos, pero algunos están **defectuosos**. Un regalo es defectuoso si su nombre contiene el carácter `#`.

Ayuda a Santa escribiendo una función que reciba una lista de nombres de regalos y devuelva una nueva lista que **solo contenga los regalos sin defectos**.


## 💡 Ejemplos

```js
const gifts1 = ['car', 'doll#arm', 'ball', '#train']
const good1 = filterGifts(gifts1)
console.log(good1)
// ['car', 'ball']

const gifts2 = ['#broken', '#rusty']
const good2 = filterGifts(gifts2)
console.log(good2)
// []

const gifts3 = []
const good3 = filterGifts(gifts3)
console.log(good3)
// []
```