<div align="center">
    <h1>Challenge #18: 🎄 Lights in Line with Diagonals</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium">
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-8%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

The Christmas lights panel 🎄✨ in the workshop has been a total success. But the elves want to go one step further: now they want to detect whether there is a **line of 4 lights of the same color** also on a **diagonal.**

The panel is still a matrix where each cell can be:

- `'.'` → light off
- `'R'` → red light
- `'G'` → green light

Now your function must return `true` if there is a line of 4 lights of the same color that are on and aligned, whether **horizontally ↔, vertically ↕ or diagonally ↘↙**.


## 💡 Examples

```js
hasFourInARow([
  ['R', '.', '.', '.'],
  ['.', 'R', '.', '.'],
  ['.', '.', 'R', '.'],
  ['.', '.', '.', 'R']
])
// true → there are 4 red lights in a ↘ diagonal

hasFourInARow([
  ['.', '.', '.', 'G'],
  ['.', '.', 'G', '.'],
  ['.', 'G', '.', '.'],
  ['G', '.', '.', '.']
])
// true → there are 4 green lights in a ↙ diagonal

hasFourInARow([
  ['R', 'R', 'R', 'R'],
  ['G', 'G', '.', '.'],
  ['.', '.', '.', '.'],
  ['.', '.', '.', '.']
])
// true → there are 4 red lights in a horizontal line

hasFourInARow([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → there are no 4 consecutive lights of the same color
```

**Note:** The board can be any size.