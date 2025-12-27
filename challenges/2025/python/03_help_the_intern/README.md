<div align="center">
    <h1>Challenge #3: 👶 Help the Intern</h1>
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

In Santa’s workshop there’s an intern elf who is learning to wrap gifts 🎁.

They’ve asked the elf to wrap boxes using only text… and they do it *more or less* correctly.

They are given two parameters:

- `size`: the size of the square gift
- `symbol`: the character the elf uses to make the border (when they don’t mess it up 😅)

The gift must meet these requirements:

- It must be a `size x size` **square**.
- The inside is always empty (filled with spaces), because the elf “doesn’t know how to draw the filling yet”.
- If `size < 2`, return an empty string: the elf tried, but the gift got lost.
- The final result must be a string with newline characters `\n`.

Yes, it’s an easy challenge… but we don’t want the intern to get fired. Right?


## 💡 Examples

```js
const g1 = drawGift(4, '*')
console.log(g1)
/*
 ****
 *  *
 *  *
 ****
 */

const g2 = drawGift(3, '#')
console.log(g2)
/*
###
# #
###
*/

const g3 = drawGift(2, '-')
console.log(g3)
/*
--
--
*/

const g4 = drawGift(1, '+')
console.log(g4)
// ""  poor intern…
```