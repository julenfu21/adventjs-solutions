<div align="center">
    <h1>Challenge #22: 🎄 The Sleigh Maze — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #22. Refer to the [main README of Challenge #22](../README.md) for more detailed instructions.


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
# <test_function> = {test_can_escape_returns_boolean, test_can_escape}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 8}

pytest test_solution.py::test_can_escape[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly implements a Breadth-First Search (BFS) algorithm to solve the maze problem.
- Helper functions are well-defined and improve readability.
- The use of a `dataclass` for `Square` is appropriate for representing coordinates.
- Edge cases like no starting position are handled with a `ValueError`.
- The BFS logic correctly uses a queue and a set for visited nodes.


### ⚠️ Weak Points

- The `get_start_position` function iterates through the entire maze even if 'S' is found early. This could be optimized by returning immediately.
- The `are_valid_coordinates` function checks `maze[row][column] != '#'` which is redundant as `get_square_neighbors` already ensures valid coordinates before appending to neighbors. This check could be moved to where neighbors are processed.


### 🧭 Next Steps

- Optimize `get_start_position` to return as soon as 'S' is found.
- Review the placement of the wall check in `are_valid_coordinates` for potential redundancy.