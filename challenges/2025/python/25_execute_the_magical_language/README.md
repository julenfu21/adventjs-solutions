<div align="center">
    <h1>Challenge #25: 🪄 Execute the Magical Language</h1>
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

We have already distributed all the gifts! Back at the workshop, preparations for next year are already beginning.

A genius elf is creating a magical programming language 🪄 that will help streamline the delivery of gifts to children in 2025.

Programs always start with the value `0`, and the language is a string where each character represents an instruction:

- `>` Moves to the next instruction
- `+` Increments the current value by 1
- `-` Decrements the current value by 1
- `[` and `]`: Loop. If the current value is `0`, jump to the instruction after `]`. If it is not 0, go back to the instruction after `[`
- `{` and `}`: Conditional. If the current value is `0`, jump to the instruction after `}`. If it is not 0, continue to the instruction after `{`

You need to return the value of the program after executing all the instructions.

**Note: A conditional can have a loop inside, and a loop can also have a conditional inside. But two loops or two conditionals are never nested.**


## 💡 Examples

```js
execute('+++') // 3
execute('+--') // -1
execute('>+++[-]') // 0
execute('>>>+{++}') // 3
execute('+{[-]+}+') // 2
execute('{+}{+}{+}') // 0
execute('------[+]++') // 2
execute('-[++{-}]+{++++}') // 5
```