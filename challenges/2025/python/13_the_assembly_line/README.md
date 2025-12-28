<div align="center">
    <h1>Challenge #13: 🏭 The Assembly Line</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium" style="margin-right:16px;">
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

Simulate the path of a gift inside a factory and return how it ends. To do this, you must create a function `runFactory(factory)`.

`factory` is a `string[]` where each cell can be:

- `>` `<` `^` `v` movements
- `.` correct exit

Keep in mind that **all rows have the same length** and that **there will be no other symbols**.

The gift **always starts at position (0,0)** (top left). At each step it reads the current cell and moves according to the direction. If it reaches a cell with a dot (`.`) it means it has correctly exited the factory.

**Result**

Return one of these values:

- `'completed'` if it reaches a `.`
- `'loop'` if it visits a position twice
- `'broken'` if it goes outside the board


## 💡 Examples

```js
runFactory([
  '>>.'
]) // 'completed'

runFactory([
  '>>>'
]) // 'broken'

runFactory([
  '>><'
]) // 'loop'

runFactory([
  '>>v',
  '..<'
]) // 'completed'

runFactory([
  '>>v',
  '<<<'
]) // 'broken'

runFactory([
  '>v.',
  '^..'
]) // 'completed'

runFactory([
  'v.',
  '^.'
]) // 'loop'
```