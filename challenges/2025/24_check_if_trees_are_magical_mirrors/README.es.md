<div align="center">
    <h1>Reto #24: 🪞 Verifica si los Árboles son Espejos Mágicos</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-8%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

En el Polo Norte, los elfos tienen **dos árboles binarios mágicos que generan energía** 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía **como espejos** 🪞.

**Dos árboles binarios son espejos si**:

- Las raíces de ambos árboles tienen el mismo valor.
- Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.

Y el árbol se representa con tres propiedades `value`, `left` y `right`. Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):

```js
const tree = {
  value: '⭐️',
  left: {
    value: '🎅'
    // left: {...}
    // right: { ... }
  },
  right: {
    value: '🎁'
    // left: { ... }
    // right: { ...&nbsp;}
  }
}
```

Santa necesita tu ayuda para verificar si los árboles están sincronizados para que la estrella pueda seguir brillando. **Debes devolver un array** donde la **primera posición indica si los árboles están sincronizados** y la **segunda posición devuelve el valor de la raíz del primer árbol**.


## 💡 Ejemplos

```js
const tree1 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

const tree2 = {
  value: '🎄',
  left: { value: '🎅' }
  right: { value: '⭐' },
}

isTreesSynchronized(tree1, tree2) // [true, '🎄']

/*
  tree1          tree2
   🎄              🎄
  / \             / \
⭐   🎅         🎅   ⭐
*/

const tree3 = {
  value: '🎄',
  left: { value: '🎅' },
  right: { value: '🎁' }
}

isTreesSynchronized(tree1, tree3) // [false, '🎄']

const tree4 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

isTreesSynchronized(tree1, tree4) // [false, '🎄']

isTreesSynchronized(
  { value: '🎅' },
  { value: '🧑‍🎄' }
) // [false, '🎅']
```