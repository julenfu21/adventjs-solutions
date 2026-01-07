<div align="center">
    <h1>Challenge #10: 📨 Depth of Christmas Magic — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #10. Refer to the [main README of Challenge #10](../README.md) for more detailed instructions.


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
# <test_function> = {test_max_depth_returns_int, test_max_depth}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 11}

pytest test_solution.py::test_max_depth[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly handles all specified edge cases for bracket balancing.
- The logic for tracking current and maximum depth is clear and efficient.
- Variable names are descriptive and follow Python conventions.
- The algorithm is optimal for this problem, with a single pass through the string.