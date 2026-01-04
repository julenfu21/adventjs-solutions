<div align="center">
    <h1>Challenge #10: 📨 Depth of Christmas Magic</h1>
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

🎄 Depth of Christmas Magic

At the North Pole, Santa Claus is reviewing the magical letters 📩✨ he receives from children all over the world. These letters use an ancient Christmas language in which the brackets `[` and `]` represent the intensity of the wish.

The deeper the nesting of the brackets, the stronger the wish. Your mission is to find out the **maximum depth** at which the `[]` are nested.

But be careful! Some letters may be **poorly written**. If the brackets are not properly balanced (if one closes before it opens, there are extra closing brackets, or closing brackets are missing), the letter is invalid and you must return `-1`.


## 💡 Examples

```js
maxDepth('[]') // -> 1
maxDepth('[[]]') // -> 2
maxDepth('[][]') // -> 1
maxDepth('[[][]]') // -> 2
maxDepth('[[[]]]') // -> 3
maxDepth('[][[]][]') // -> 2

maxDepth('][') // -> -1 (closes before opening)
maxDepth('[[[') // -> -1 (missing closing brackets)
maxDepth('[]]]') // -> -1 (extra closing brackets)
maxDepth('[][][') // -> -1 (one remains unclosed)
```