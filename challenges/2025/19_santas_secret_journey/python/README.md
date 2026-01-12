<div align="center">
    <h1>Challenge #19: 🎄 Santa's Secret Journey — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #19. Refer to the [main README of Challenge #19](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-8%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_reveal_santa_route_returns_list, test_reveal_santa_route}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 5}

pytest test_solution.py::test_reveal_santa_route[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly reconstructs Santa's route by iteratively finding the next segment.
- The use of a helper function `get_next_trip_segment` improves readability and modularity.
- The solution handles cases where segments might not belong to the main route by simply not including them.
- Variable names are descriptive and follow Python conventions.
- The code is clean, well-structured, and easy to understand.