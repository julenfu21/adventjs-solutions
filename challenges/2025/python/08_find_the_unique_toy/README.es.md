<div align="center">
    <h1>Reto #8: 🎁 Encuentra el Juguete Único</h1>
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

Santa 🎅 quiere saber cuál es la primera letra no repetida en el nombre de un juguete 🎁.

Escribe una función que reciba un `string` y devuelva la primera letra que no se repite, ignorando mayúsculas y minúsculas al contar, pero devolviendo la letra tal como aparece en el string.

Si no hay ninguna, devuelve una cadena vacía ("").


## 💡 Ejemplos

```js
findUniqueToy('Gift') // 'G'
// ℹ️ La G es la primera letra que no se repite
// y la devolvemos tal y como aparece

findUniqueToy('sS') // ''
// ℹ️ Las letras se repiten, ya que no diferencia mayúsculas

findUniqueToy('reindeeR') // 'i'
// ℹ️ La r se repite (aunque sea en mayúscula)
// y la e también, así que la primera es la 'i'

// Más casos:
findUniqueToy('AaBbCc') // ''
findUniqueToy('abcDEF') // 'a'
findUniqueToy('aAaAaAF') // 'F'
findUniqueToy('sTreSS') // 'T'
findUniqueToy('z') // 'z'
```