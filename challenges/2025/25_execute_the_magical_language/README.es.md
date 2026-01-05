<div align="center">
    <h1>Reto #25: 🪄 Ejecuta el Lenguaje Mágico</h1>
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

¡Ya hemos repartido todos los regalos! De vuelta al taller, ya comienzan los preparativos para el año que viene.

Un elfo genio está creando un lenguaje de programación mágico 🪄, que ayudará a simplificar la entrega de regalos a los niños en 2025.

Los programas siempre empiezan con el valor `0` y el lenguaje es una cadena de texto donde cada caracter representa una instrucción:

- `>` Se mueve a la siguiente instrucción
- `+` Incrementa en 1 el valor actual
- `-` Decrementa en 1 el valor actual
- `[` y `]`: Bucle. Si el valor actual es `0`, salta a la instrucción después de `]`. Si no es 0, vuelve a la instrucción después de `[`
- `{` y `}`: Condicional. Si el valor actual es `0`, salta a la instrucción después de `}`. Si no es 0, sigue a la instrucción después de `{`

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