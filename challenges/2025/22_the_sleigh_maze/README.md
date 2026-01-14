<div align="center">
    <h1>Challenge #22: 🎄 The Sleigh Maze</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-HARD-red" alt="Difficulty: Hard">
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

Santa Claus 🎅 is testing a new **sleigh simulator** inside a maze in the workshop. The maze is represented as a matrix of characters.

Your task is to implement a function that determines if it is possible to reach the exit (`E`) starting from the initial position (`S`).

**Maze rules:**

- `S`: Santa's initial position.
- `E`: Maze exit.
- `.`: Free path.
- `#`: Wall (blocks the path).
- Allowed movements: **up, down, left, and right.**
- There is only one `S` and one `E`.


## 💡 Examples

```js
canEscape([
  ['S', '.', '#', '.'],
  ['#', '.', '#', '.'],
  ['.', '.', '.', '.'],
  ['#', '#', '#', 'E']
])
// → true

canEscape([
  ['S', '#', '#'],
  ['.', '#', '.'],
  ['.', '#', 'E']
])
// → false

canEscape([
  ['S', 'E']
])
// → true

canEscape([
  ['S', '.', '.', '.', '.'],
  ['#', '#', '#', '#', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', '#', '#', '#', '#'],
  ['.', '.', '.', '.', 'E']
])
// → true

canEscape([
  ['S', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#'],
  ['.', '.', 'E']
])
// → false
```

**Things to keep in mind:**

- You don't need to return the path, just if it is possible to arrive.
- Santa cannot leave the boundaries of the maze.
- You can pass through the same cell multiple times.

**Tip**: This problem can be solved in several ways, but search algorithms like **BFS** (Breadth-First Search) or **DFS** (Depth-First Search) are ideal for these types of challenges.
