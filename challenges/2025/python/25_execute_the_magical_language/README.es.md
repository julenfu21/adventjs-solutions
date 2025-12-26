<div align="center">
  <h1>Reto #25: 🪄 Ejecuta el Lenguaje Mágico</h1>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Dificultad-MEDIO-yellow" alt="Dificultad: Medio" style="margin-right:16px;">
  <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8">
</p>
<br>


## 🌐 Leer en Otros Idiomas

<p align="center">
  <a href="README.md">
    <img src="https://img.shields.io/badge/Language-en-red.svg" alt="Inglés">
  </a>
</p>


## 🎯 Instrucciones

¡Ya hemos repartido todos los regalos! De vuelta al taller, ya comienzan los preparativos para el año que viene.

Un elfo genio está creando un lenguaje de programación mágico 🪄, que ayudará a simplificar la entrega de regalos a los niños en 2025.

Los programas siempre empiezan con el valor `0` y el lenguaje es una cadena de texto donde cada caracter representa una instrucción:

- `>` Se mueve a la siguiente instrucción
- `+` Incrementa en 1 el valor actual
- `-` Decrementa en 1 el valor actual
- `[` and `]`: Bucle. Si el valor actual es `0`, salta a la instrucción después de `]`. Si no es 0, vuelve a la instrucción después de `[`
- `{` and `}`: Condicional. Si el valor actual es `0`, salta a la instrucción después de `}`. Si no es 0, sigue a la instrucción después de `{`

Tienes que devolver el valor del programa tras ejecutar todas las instrucciones.

**Nota: Un condicional puede tener un bucle dentro y también un bucle puede tener un condicional. Pero nunca se anidan dos bucles o dos condicionales.**


## 💡 Ejemplos

```js
execute('+++') // 3
execute('+--') // -1
execute('>+++[-]') // 0
execute('>>>+{++}') // 3
execute('+{[-]+}+') // 2
execute('{+}{+}{+}') // 0
execute('------[+]++') // 2
execute('-[++{-}]+{++++}') // 5
```