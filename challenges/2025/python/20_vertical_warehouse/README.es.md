<div align="center">
    <h1>Reto #20: 🎁 El Almacén Vertical</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-FÁCIL-brightgreen" alt="Dificultad: Fácil" style="margin-right:16px;">
    <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8">
</p>
<br>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 🎯 Instrucciones

En el taller de Santa, los elfos están guardando regalos 🎁 en un **almacén vertical**. Los regalos se dejan caer uno a uno por una columna y se van apilando.

El almacén es una matriz con `#` regalos y `.` espacios vacíos. Debes crear una función `dropGifts` que reciba el estado del almacén y un array con las columnas donde se dejan caer los regalos.

**Reglas de la caída:**

- El regalo cae por la columna indicada desde arriba.
- Se coloca en la **celda vacía** (`.`) más baja de esa columna.
- Si la columna está llena, el regalo se ignora.



## 💡 Ejemplos

```js
dropGifts(
  [
    ['.', '.', '.'],
    ['.', '#', '.'],
    ['#', '#', '.']
  ],
  [0]
)
/*
[
  ['.', '.', '.'],
  ['#', '#', '.'],
  ['#', '#', '.']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['#', '#', '#']
  ],
  [0, 2]
)
/*
[
  ['#', '.', '.'],
  ['#', '#', '#'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
  ],
  [0, 1, 2]
)
/*
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['#', '#']
    ['#', '#']
  ],
  [0, 0]
)
/*
[
  ['#', '#']
  ['#', '#']
]
```