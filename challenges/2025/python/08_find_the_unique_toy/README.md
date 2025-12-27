<div align="center">
    <h1>Challenge #8: 🎁 Find the Unique Toy</h1>
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

Santa 🎅 wants to know what the first non-repeated letter is in a toy's name 🎁.

Write a function that takes a `string` and returns the first letter that is not repeated, ignoring uppercase and lowercase when counting, but returning the letter as it appears in the string.

If there is none, return an empty string ("").


## 💡 Examples

```js
findUniqueToy('Gift') // 'G'
// ℹ️ The G is the first letter that is not repeated
// and we return it exactly as it appears

findUniqueToy('sS') // ''
// ℹ️ The letters are repeated, since it doesn't distinguish uppercase

findUniqueToy('reindeeR') // 'i'
// ℹ️ The r is repeated (even if it's uppercase)
// and the e as well, so the first one is 'i'

// More cases:
findUniqueToy('AaBbCc') // ''
findUniqueToy('abcDEF') // 'a'
findUniqueToy('aAaAaAF') // 'F'
findUniqueToy('sTreSS') // 'T'
findUniqueToy('z') // 'z'
```