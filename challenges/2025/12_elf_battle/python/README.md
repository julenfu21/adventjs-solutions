<div align="center">
    <h1>Challenge #12: ⚔️ Elf Battle — Python</h1>
</div>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 📖 Overview

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #12. Refer to the [main README of Challenge #12](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-6%2F8-lightcoral" alt="Score: 5-6" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_elf_battle_returns_int, test_elf_battle}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 8}

pytest test_solution.py::test_elf_battle[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly implements the battle logic and handles simultaneous moves.
- Helper functions `attack_other_player` and `has_player_lost` improve readability.
- The use of `zip` to iterate through moves is efficient and clear.
- Edge cases like simultaneous loss and the battle ending mid-round are handled.


### ⚠️ Weak Points

- The cyclomatic complexity is high due to nested conditional logic within the loop and helper functions.


### 🧭 Next Steps

- Consider refactoring the conditional logic within `attack_other_player` to reduce nesting and improve clarity. For example, a series of `if/elif/else` statements might be more straightforward than multiple independent `if` checks.