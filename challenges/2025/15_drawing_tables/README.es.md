<div align="center">
    <h1>Reto #15: ✏️ Dibujando Tablas</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Puntuación-6%2F8-lightcoral" alt="Puntuación: 5-6" style="vertical-align: middle;"> | [Ir a la Implementación](python/README.es.md) |


## 🎯 Instrucciones

**Al Polo Norte ha llegado ChatGPT** y el elfo *Sam Elfman* está trabajando en una aplicación de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función `drawTable` que reciba un **array de objetos** y lo convierta en una **tabla de texto**.

La tabla dibujada debe tener:

Cabecera con letras de columna (`A`, `B`, `C`…).
El contenido de la tabla son los valores de los objetos.
Los valores deben estar alineados a la izquierda.
Los campos dejan siempre un espacio a la izquierda.
Los campos dejan a la derecha el espacio necesario para alinear la caja.

La función recibe un segundo parámetro `sortBy` que indica el nombre del campo por el que se deben **ordenar las filas**. El orden será **alfabético ascendente** si los valores son strings y **numérico ascendente** si son números.

Mira el ejemplo para ver cómo debes dibujar la tabla:


## 💡 Ejemplos

```js
drawTable(
  [
    { name: 'Charlie', city: 'New York' },
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' }
  ],
  'name'
)
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

drawTable(
  [
    { gift: 'Book', quantity: 5 },
    { gift: 'Music CD', quantity: 1 },
    { gift: 'Doll', quantity: 10 }
  ],
  'quantity'
)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
```