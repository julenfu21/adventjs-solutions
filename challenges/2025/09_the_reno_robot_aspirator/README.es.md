<div align="center">
    <h1>Reto #9: 🦌 El Reno Robot Aspirador</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-DIFÍCIL-red" alt="Dificultad: Difícil">
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

Los elfos han construido un **reno 🦌 robot aspirador** (`@`) para limpiar un poco el taller de cara a las navidades.

El reno se mueve sobre un tablero para **recoger cosas del suelo** (`*`) y debe **evitar obstáculos** (`#`).

Recibirás dos parámetros:

- `board`: un `string` que representa el tablero.
- `moves`: un `string` con los movimientos: `'L'` (izquierda), `'R'` (derecha), `'U'` (arriba), `'D'` (abajo).

**Reglas del movimiento**:

- Si el reno **recoge algo del suelo** (`*`) durante los movimientos → devuelve `'success'`.
- Si el reno se **sale del tablero** o **choca contra un obstáculo** (`#`) → devuelve `'crash'`.
- Si el reno **no recoge nada ni se estrella** → devuelve `'fail'`.

Ten en cuenta que si el reno **recoge algo del suelo**, ya es `'success'`, indepentientemente de si en movimientos posteriores se chocase con un obstáculo o saliese del tablero.

**Importante**: Ten en cuenta que en el `board` la primera y última línea están en blanco y deben descartarse.


## 💡 Ejemplos

```js
const board = `
.....
.*#.*
.@...
.....
`

moveReno(board, 'D')
// ➞ 'fail' -> se mueve pero no recoge nada

moveReno(board, 'U')
// ➞ 'success' -> recoge algo (*) justo encima

moveReno(board, 'RU')
// ➞ 'crash' -> choca contra un obstáculo (#)

moveReno(board, 'RRRUU')
// ➞ 'success' -> recoge algo (*)

moveReno(board, 'DD')
// ➞ 'crash' -> se choca con la parte de abajo del tablero

moveReno(board, 'UUU')
// ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba

moveReno(board, 'RR')
// ➞ 'fail' -> se mueve pero no recoge nada
```