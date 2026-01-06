<div align="center">
    <h1>Reto #4: 🧮 Descifra el PIN de Santa</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-6%2F8-lightcoral" alt="Puntuación: 5-6" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

Los elfos han encontrado el **código cifrado** que protege la puerta del taller de Santa 🔐. El PIN tiene **4 dígitos**, y está escondido dentro de bloques como estos:

```
[1++][2-][3+][<]
```

**Escribe una función que descifre el PIN a partir del código.**

El código está formado por bloques entre corchetes `[...]` y cada bloque genera un dígito del PIN.

Un bloque normal tiene la forma `[nOP...]`, donde `n` es un número (0-9) y después puede haber una lista de operaciones (opcionales).

Las operaciones se aplican en orden al número y son:

- `+` suma 1
- `-` resta 1

El resultado siempre es un dígito (aritmética mod 10), por ejemplo `9 + 1 → 0` y `0 - 1 → 9`.

También existe el bloque especial `[<]`, que repite el dígito del bloque anterior.

Si al final hay menos de 4 dígitos, se debe devolver `null`.


## 💡 Ejemplos

```js
decodeSantaPin('[1++][2-][3+][<]')
// "3144"

decodeSantaPin('[9+][0-][4][<]')
// "0944"

decodeSantaPin('[1+][2-]')
// null (solo 2 dígitos)
```