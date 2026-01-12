<div align="center">
    <h1>Reto #18: 🎄 Luces en Línea con Diagonales</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-MEDIO-yellow" alt="Dificultad: Medio">
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-8%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

El panel de luces navideñas 🎄✨ del taller ha sido un éxito total. Pero los elfos quieren ir un paso más allá: ahora quieren detectar si hay una **línea de 4 luces del mismo color** también en **diagonal**.

El panel sigue siendo una matriz donde cada celda puede ser:

- `'.'` → luz apagada
- `'R'` → luz roja
- `'G'` → luz verde

Ahora tu función debe devolver `true` si existe una línea de 4 luces del mismo color encendidas y alineadas, ya sea **horizontal ↔, vertical ↕ o diagonal ↘↙.**


## 💡 Ejemplos

```js
hasFourInARow([
  ['R', '.', '.', '.'],
  ['.', 'R', '.', '.'],
  ['.', '.', 'R', '.'],
  ['.', '.', '.', 'R']
])
// true → hay 4 luces rojas en diagonal ↘

hasFourInARow([
  ['.', '.', '.', 'G'],
  ['.', '.', 'G', '.'],
  ['.', 'G', '.', '.'],
  ['G', '.', '.', '.']
])
// true → hay 4 luces verdes en diagonal ↙

hasFourInARow([
  ['R', 'R', 'R', 'R'],
  ['G', 'G', '.', '.'],
  ['.', '.', '.', '.'],
  ['.', '.', '.', '.']
])
// true → hay 4 luces rojas en horizontal

hasFourInARow([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → no hay 4 luces del mismo color seguidas
```

**Nota:** El tablero puede ser de cualquier tamaño.