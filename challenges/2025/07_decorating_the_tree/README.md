<div align="center">
    <h1>Challenge #7: 🎄 Decorating the Tree</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium">
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

It’s time to decorate the **Christmas tree** 🎄! Write a function that receives:

- `height` → the height of the tree (number of rows).
- `ornament` → the ornament character (for example, `"o"` or `"@"`).
- `frequency` → how often (in asterisk positions) the ornament appears.

The tree is drawn with asterisks `*`, but **every `frequency` positions**, the asterisk is replaced by the ornament.

The position counting starts at 1, from the top to the bottom, left to right. If `frequency` is 2, the ornaments appear in positions 2, 4, 6, etc.

The tree must be centered and have a one-line trunk `#` at the end.


## 💡 Examples

```js
drawTree(5, 'o', 2)
//     *
//    o*o
//   *o*o*
//  o*o*o*o
// *o*o*o*o*
//     #

drawTree(3, '@', 3)
//   *
//  *@*
// *@**@
//   #

drawTree(4, '+', 1)
//    +
//   +++
//  +++++
// +++++++
//    #
```