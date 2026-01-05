<div align="center">
    <h1>Reto #17: 🎄 El Panel de Luces Navideñas</h1>
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

En el Polo Norte han montado un **panel de luces navideñas** 🎄✨ para decorar el taller. Cada luz puede estar encendida con un color o apagada.

El panel se representa como una **matriz** donde cada celda puede ser:

- `'.'` → luz apagada
- `'R'` → luz roja
- `'G'` → luz verde

Los elfos quieren saber si en el panel existe una **línea de 4 luces del mismo color** encendidas y **alineadas** (solo horizontal ↔ o vertical ↕). Las luces apagadas (`'.'`) no cuentan.


## 💡 Ejemplos

```js
hasFourLights([
  ['.', '.', '.', '.', '.'],
  ['R', 'R', 'R', 'R', '.'],
  ['G', 'G', '.', '.', '.']
])
// true → hay 4 luces rojas en horizontal

hasFourLights([
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.']
])
// true → hay 4 luces verdes en vertical

hasFourLights([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → no hay 4 luces del mismo color seguidas
```

**Nota:** El tablero puede ser de cualquier tamaño. No hay diagonales.