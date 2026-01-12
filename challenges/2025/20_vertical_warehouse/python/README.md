<div align="center">
    <h1>Challenge #20: 🎁 Vertical Warehouse — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #20. Refer to the [main README of Challenge #20](../README.md) for more detailed instructions.


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
# <test_function> = {test_drop_gifts_returns_list, test_drop_gifts}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 7}

pytest test_solution.py::test_drop_gifts[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly implements the gift dropping logic.
- The helper function `get_lowest_empty_cell_row_index` is well-defined and improves readability.
- Variable names are descriptive and follow Python conventions.
- The code handles edge cases where a column might be full.
- The solution is efficient for the given problem constraints.