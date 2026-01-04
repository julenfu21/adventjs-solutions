<div align="center">
    <h1>Challenge #1: 🎁 Filter the Defective Gifts — Python</h1>
</div>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 📖 Overview

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #1. Refer to the [main README of Challenge #1](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-6%2F8-lightcoral" alt="Score: 5-6" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_filter_gifts_returns_list, test_filter_gifts}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {0 - 4}

pytest test_solution.py::test_filter_gifts[gifts<index>-expected_gifts<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code is concise and effectively uses a list comprehension for filtering.
- It correctly handles edge cases like empty lists.
- The logic is straightforward and easy to understand.