<div align="center">
    <h1>Challenge #16: 🎁 Packing Gifts for Santa — Python</h1>
</div>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish" style="margin-right:16px;">
    </a>
    <a href="README.eu.md">
        <img src="https://img.shields.io/badge/Language-eu-green.svg" alt="Basque">
    </a>
</p>


## 📖 Overview

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #16. Refer to the [main README of Challenge #16](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_pack_gifts_returns_int, test_pack_gifts}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 12}

pytest test_solution.py::test_pack_gifts[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly handles the edge case of an empty gift list.
- The logic for determining sleigh usage is clear and efficient.
- The function correctly identifies and returns null when a gift exceeds the maximum sleigh weight.
- Variable names are descriptive and follow Python conventions.