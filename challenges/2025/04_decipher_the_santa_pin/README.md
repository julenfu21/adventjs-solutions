<div align="center">
    <h1>Challenge #4: 🧮 Decipher the Santa PIN</h1>
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
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-6%2F8-lightcoral" alt="Score: 5-6" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

The elves have found the **encrypted code** that protects the door to Santa’s workshop 🔐. The PIN has **4 digits**, and it is hidden inside blocks like these:

```
[1++][2-][3+][<]
```

**Write a function that deciphers the PIN from the code.**

The code is made up of blocks between brackets `[...]` and each block generates one digit of the PIN.

A normal block has the form `[nOP...]`, where `n` is a number (0-9) and after it there can be a list of (optional) operations.

The operations are applied in order to the number and are:

- `+` adds 1
- `-` substracts 1

The result is always a digit (mod 10 arithmetic), for example `9 + 1 → 0` and `0 - 1 → 9`.

There is also the special block `[<]`, which repeats the digit from the previous block.

If in the end there are fewer than 4 digits, you must return `null`.


## 💡 Examples

```js
decodeSantaPin('[1++][2-][3+][<]')
// "3144"

decodeSantaPin('[9+][0-][4][<]')
// "0944"

decodeSantaPin('[1+][2-]')
// null (only 2 digits)
```