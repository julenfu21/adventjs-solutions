<div align="center">
    <h1>Challenge #9: 🦌 The Reno Robot Aspirator — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #9. Refer to the [main README of Challenge #9](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-HARD-red" alt="Difficulty: Hard" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_move_reno_returns_string, test_move_reno}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 9}

pytest test_solution.py::test_move_reno[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly identifies the reindeer's starting position.
- It accurately simulates the reindeer's movement based on the input moves.
- Edge cases like going off-board or hitting obstacles are handled correctly.
- The logic for returning 'success' upon picking up an item is sound.
- The code is well-structured and easy to follow.


### ⚠️ Weak Points:

- The cyclomatic complexity is slightly high (14), which could be reduced by refactoring some conditional logic.


### 🧭 Next Steps:

- Consider refactoring the movement logic and boundary/obstacle checks to reduce cyclomatic complexity. For example, a helper function could encapsulate the state checking after each move.