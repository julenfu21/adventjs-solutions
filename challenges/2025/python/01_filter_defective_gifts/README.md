<div align="center">
    <h1>Challenge #1: 🎁 Filter the Defective Gifts</h1>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy" style="margin-right:16px;">
  <img src="https://img.shields.io/badge/Score-6%2F8-lightcoral" alt="Score: 5-6">
</p>
<br>


## 🌐 Other Languages

<p align="center">
  <a href="README.es.md">
      <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
  </a>
</p>


## 🎯 Instructions

Santa has received a list of gifts, but some are **defective**. A gift is defective if its name contains the `#` character.

Help Santa by writing a function that takes a list of gift names and returns a new list that **only contains the non-defective gifts**.


## 💡 Examples

```js
const gifts1 = ['car', 'doll#arm', 'ball', '#train']
const good1 = filterGifts(gifts1)
console.log(good1)
// ['car', 'ball']

const gifts2 = ['#broken', '#rusty']
const good2 = filterGifts(gifts2)
console.log(good2)
// []

const gifts3 = []
const good3 = filterGifts(gifts3)
console.log(good3)
// []
```