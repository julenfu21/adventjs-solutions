<div align="center">
    <h1>Challenge #3: 👶 Help the Intern — Python</h1>
</div>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 📖 Overview

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #3. Refer to the [main README of Challenge #3](../README.md) for more detailed instructions.


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
# <test_function> = {test_draw_gift_returns_string, test_draw_gift}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 6}

pytest test_solution.py::test_draw_gift[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly handles the edge case where size is less than 2.
- The logic for constructing the top, bottom, and middle rows is clear and efficient.
- Variable names are descriptive and follow Python conventions.
- The use of string multiplication and list comprehension is idiomatic and readable.
- The final string is correctly formatted with newline characters.