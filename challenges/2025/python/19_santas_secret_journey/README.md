<div align="center">
    <h1>Challenge #19: 🎄 Santa's Secret Journey</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy" style="margin-right:16px;">
    <img src="https://img.shields.io/badge/Score-8%2F8-blueviolet" alt="Score: 7-8">
</p>
<br>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 🎯 Instructions

The sleigh’s GPS has gone crazy! 😱 Santa Claus has the **segments of his trip**, but they’re all out of order.

Your mission is to **reconstruct the complete route** from the origin to the final destination.

Keep in mind: **The first element of the array is always the first segment of the trip**. From there, you must keep connecting destinations to the next origins.


## 💡 Examples

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

🔎 **Keep in mind:**

- There are no duplicate routes or cycles in Santa’s path.
- There may be segments that don’t belong to the route; these must be ignored.
