<div align="center">
    <h1>Challenge #14: 🗃️ Find the Gift Path</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy" style="margin-right:16px;">
    <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8">
</p>
<br>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 🎯 Instructions

At the North Pole, the elves have simplified their storage system to avoid mistakes. They now keep the presents in a **magical object with limited depth**, where **each value appears only once**.

Santa needs a quick way to know **which path of keys** he must follow to find a specific present.

Your task is to write a function that, given an object and a value, returns the **array of keys** that must be traversed to reach that value.

**Rules:**

- The object has **at most 3 levels of depth**.
- The value to search for **appears at most once**.
- The object only contains **other objects and primitive values** (strings, numbers, booleans).
- If the value does not exist, return an empty array.


## 💡 Examples

```js
const workshop = {
  storage: {
    shelf: {
      box1: 'train',
      box2: 'switch'
    },
    box: 'car'
  },
  gift: 'doll'
}

findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']

findGiftPath(workshop, 'switch')
// ➜ ['storage', 'shelf', 'box2']

findGiftPath(workshop, 'car')
// ➜ ['storage', 'box']

findGiftPath(workshop, 'doll')
// ➜ ['gift']

findGiftPath(workshop, 'plane')
// ➜ []
```