<div align="center">
    <h1>Challenge #6: 🧤 Matching Gloves — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #6. Refer to the [main README of Challenge #6](../README.md) for more detailed instructions.


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
# <test_function> = {test_match_gloves_returns_list, test_match_gloves}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 9}

pytest test_solution.py::test_match_gloves[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly identifies and counts left and right gloves of the same color.
- It efficiently uses `defaultdict` to store glove counts.
- The logic for matching pairs and appending to the result list is sound.
- The function returns an empty list when no pairs are found, as required.
- The code adheres to Python best practices with clear variable names and formatting.