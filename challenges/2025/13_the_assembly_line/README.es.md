<div align="center">
    <h1>Reto #13: 🏭 La Cadena de Montaje</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-MEDIO-yellow" alt="Dificultad: Medio">
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

Simula el recorrido de un regalo dentro de una fábrica y devuelve cómo termina. Para ello debes crear una función `runFactory(factory)`.

`factory` es un `string[]` donde cada celda puede ser:

- `>` `<` `^` `v` movimientos
- `.` salida correcta

Ten en cuenta que **todas las filas tienen la misma longitud** y que **no habrá otros símbolos**.

El regalo **siempre empieza en la posición (0,0)** (arriba a la izquierda). En cada paso lee la celda actual y se mueve según la dirección. Si llega a una celda con un punto (`.`) significa que ha salido correctamente de la fábrica.

**Resultado**

Devuelve uno de estos valores:

- `'completed'` si llega a un `.`
- `'loop'` si visita una posición dos veces
- `'broken'` si sale fuera del tablero


## 💡 Ejemplos

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