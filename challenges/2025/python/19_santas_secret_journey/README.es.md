<div align="center">
    <h1>Reto #19: 🎄 El Viaje Secreto de Papá Noel</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Dificultad-FÁCIL-brightgreen" alt="Dificultad: Fácil" style="margin-right:16px;">
    <img src="https://img.shields.io/badge/Puntuación-8%2F8-blueviolet" alt="Puntuación: 7-8">
</p>
<br>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 🎯 Instrucciones

¡El GPS del trineo se ha vuelto loco! 😱 Papá Noel tiene los **tramos de su viaje**, pero están todos desordenados.

Tu misión es **reconstruir la ruta completa** desde el origen hasta el destino final.

Ten en cuenta: **El primer elemento del array es siempre el primer tramo del viaje**. A partir de ahí, debes ir conectando los destinos con los siguientes orígenes.


## 💡 Ejemplos

```js
revealSantaRoute([
  ['MEX', 'CAN'],
  ['UK', 'GER'],
  ['CAN', 'UK']
])
// → ['MEX', 'CAN', 'UK', 'GER']

revealSantaRoute([
  ['USA', 'BRA'],
  ['JPN', 'PHL'],
  ['BRA', 'UAE'],
  ['UAE', 'JPN'],
  ['CMX', 'HKN']
])
// → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']

revealSantaRoute([
  ['STA', 'HYD'],
  ['ESP', 'CHN']
])
// → ['STA', 'HYD']
```

🔎 **A tener en cuenta**:

- No hay rutas duplicadas ni ciclos en el camino de Papá Noel.
- Puede haber tramos que no pertenezcan a la ruta; estos deben ignorarse.
