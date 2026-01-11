<div align="center">
    <h1>Reto #14: 🗃️ Encuentra el Camino al Regalo</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

En el Polo Norte, los elfos han simplificado su sistema de almacenamiento para evitar errores. Ahora guardan los regalos en un **objeto mágico con profundidad limitada**, donde **cada valor aparece una sola vez**.

Santa necesita una forma rápida de saber **qué camino de claves** debe seguir para encontrar un regalo concreto.

Tu tarea es escribir una función que, dado un objeto y un valor, devuelva el **array de claves** que hay que recorrer para llegar a ese valor.

**Reglas:**

- El objeto tiene **como máximo 3 niveles de profundidad**.
- El valor a buscar **aparece como mucho una vez**.
- El objeto solo contiene **otros objetos y valores primitivos** (strings, numbers, booleans).
- Si el valor no existe, devuelve un array vacío.


## 💡 Ejemplos

```js
const workshop = {
  storage: {
    shelf: {
      box1: 'train',
      box2: 'switch'
    },
    box: 'car'
  },
  gift: 'doll'
}

findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']

findGiftPath(workshop, 'switch')
// ➜ ['storage', 'shelf', 'box2']

findGiftPath(workshop, 'car')
// ➜ ['storage', 'box']

findGiftPath(workshop, 'doll')
// ➜ ['gift']

findGiftPath(workshop, 'plane')
// ➜ []
```