<div align="center">
    <h1>Challenge #11: 📹 Unwatched Gifts</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

The Grinch wants to steal the Christmas presents from the warehouse. To do this, he needs to know **which presents are not under surveillance**.

The warehouse is represented as an array of strings (`string[]`), where **each present** (`*`) **is protected if its position is next to a camera** (`#`). Each empty space is represented with a **dot** (`.`).

Your task is to **count how many presents are not under surveillance**, meaning they do not have any adjacent camera (up, down, left, or right).

Keep in mind: *only the 4 cardinal directions are considered "adjacent", not diagonals*.

Presents in the corners or at the edges can be unguarded, as long as they do not have cameras directly next to them.


## 💡 Examples

```js
findUnsafeGifts([
  '.*.',
  '*#*',
  '.*.'
]) // ➞ 0

// All presents are next to a camera

findUnsafeGifts([
  '...',
  '.*.',
  '...'
]) // ➞ 1

// This present has no cameras around

findUnsafeGifts([
  '*.*',
  '...',
  '*#*'
]) // ➞ 2
// The presents in the top corners have no cameras around

findUnsafeGifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]) // ➞ 4

// The four presents have no cameras, because they are diagonal to the camera
```