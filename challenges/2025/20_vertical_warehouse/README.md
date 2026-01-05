<div align="center">
    <h1>Challenge #20: 🎁 Vertical Warehouse</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy">
</p>
<br>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 💻 Implementations & Scores

| Language | Score | Implementation |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

In Santa's workshop, the elves are storing gifts 🎁 in a **vertical warehouse**. The gifts are dropped one by one through a column and start stacking up.

The warehouse is a matrix with `#` gifts and `.` empty spaces. You must create a `dropGifts` function that receives the warehouse state and an array with the columns where the gifts are dropped.

**Falling rules:**

- The gift falls through the indicated column from the top.
- It is placed in the **lowest empty cell** (`.`) of that column.
- If the column is full, the gift is ignored.


## 💡 Examples

```js
dropGifts(
  [
    ['.', '.', '.'],
    ['.', '#', '.'],
    ['#', '#', '.']
  ],
  [0]
)
/*
[
  ['.', '.', '.'],
  ['#', '#', '.'],
  ['#', '#', '.']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['#', '#', '#']
  ],
  [0, 2]
)
/*
[
  ['#', '.', '.'],
  ['#', '#', '#'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
  ],
  [0, 1, 2]
)
/*
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['#', '#']
    ['#', '#']
  ],
  [0, 0]
)
/*
[
  ['#', '#']
  ['#', '#']
]
```
