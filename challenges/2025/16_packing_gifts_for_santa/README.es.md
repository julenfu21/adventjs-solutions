<div align="center">
    <h1>Reto #16: 🎁 Empaquetando Regalos para Santa</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-FÁCIL-brightgreen" alt="Dificultad: Fácil">
</p>
<br>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 💻 Implementaciones y Puntuaciones

| Lenguaje | Puntuación | Implementación |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

Santa quiere repartir regalos de la forma **más eficiente posible** 🎁. Tiene una lista de regalos, cada uno con un **peso**, y un trineo que solo puede cargar hasta un **peso máximo**.

Los regalos se entregan **en orden**, y Santa no puede cambiar ese orden. Cuando un regalo no cabe en el trineo actual, Santa envía el trineo y prepara uno nuevo.

Tu tarea es escribir una función que calcule el **número mínimo de trineos necesarios** para entregar todos los regalos.

Eso sí, ten en cuenta que a veces hay un regalo que no cabe en el trineo, entonces hay que devolver `null` porque ese trineo no sirve para ese pack de regalos.


## 💡 Ejemplos

```js
packGifts([2, 3, 4, 1], 5)
// 2 trineos
// Trineo 1: 2 + 3 = 5
// Trineo 2: 4 + 1 = 5

packGifts([3, 3, 2, 1], 3)
// 3 trineos
// Trineo 1: 3
// Trineo 2: 3
// Trineo 3: 2 + 1 = 3

packGifts([1, 1, 1, 1], 2)
// 2 trineos
// Trineo 1: 1 + 1 = 2
// Trineo 2: 1 + 1 = 2

packGifts([5, 6, 1], 5)
// null
// Hay un regalo de peso 6 que no cabe

packGifts([], 10)
// 0 trineos
// No hay regalos que entregar
```