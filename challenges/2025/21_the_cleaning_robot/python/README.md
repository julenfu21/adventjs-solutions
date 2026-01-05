<div align="center">
    <h1>Challenge #21: 🤖 The Cleaning Robot — Python</h1>
</div>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 📖 Overview

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #21. Refer to the [main README of Challenge #21](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_clear_gifts_returns_list, test_clear_gifts}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 6}

pytest test_solution.py::test_clear_gifts[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly implements the logic for dropping gifts and clearing full rows.
- The helper function `get_lowest_empty_cell_row_index` is well-defined and improves readability.
- Variable names are descriptive and follow Python conventions.
- The code handles edge cases such as full columns gracefully.