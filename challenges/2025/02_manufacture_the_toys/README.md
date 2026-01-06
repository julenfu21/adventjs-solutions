<div align="center">
    <h1>Challenge #2: 🏭 Manufacture the Toys</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy">
</p>
<br>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish" style="margin-right:16px;">
    </a>
    <a href="README.eu.md">
        <img src="https://img.shields.io/badge/Language-eu-green.svg" alt="Basque">
    </a>
</p>


## 💻 Implementations & Scores

| Language | Score | Implementation |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-6%2F8-lightcoral" alt="Score: 5-6" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

Santa's factory has started to receive the toy **production list**. Each line indicates **which toy** must be manufactured and **how many units**.

The elves, as always, have messed things up: they wrote down some toys with quantities that don't make any sense.

You have a list of objects with this structure:

- `toy`: the name of the toy (string)
- `quantity`: how many units must be manufactured (number)

Your task is to write a function that takes this list and returns **an array of strings** with:

- Each toy repeated as many times as indicated by `quantity`
- In the same order in which they appear in the original list
- Ignoring toys with invalid quantities (less than or equal to 0, or not a number)


## 💡 Examples

```js
const production1 = [
  { toy: 'car', quantity: 3 },
  { toy: 'doll', quantity: 1 },
  { toy: 'ball', quantity: 2 }
]

const result1 = manufactureGifts(production1)
console.log(result1)
// ['car', 'car', 'car', 'doll', 'ball', 'ball']

const production2 = [
  { toy: 'train', quantity: 0 }, // not manufactured
  { toy: 'bear', quantity: -2 }, // neither
  { toy: 'puzzle', quantity: 1 }
]

const result2 = manufactureGifts(production2)
console.log(result2)
// ['puzzle']

const production3 = []
const result3 = manufactureGifts(production3)
console.log(result3)
// []
```