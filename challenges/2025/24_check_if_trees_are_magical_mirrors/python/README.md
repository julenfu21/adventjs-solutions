<div align="center">
    <h1>Challenge #24: 🪞 Check if Trees are Magical Mirrors — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #24. Refer to the [main README of Challenge #24](../README.md) for more detailed instructions.


## 📊 Challenge Details

| Difficulty | Score |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Score-8%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> |


## 💻 Solution

See [`solution.py`](solution.py) for the implementation.


## 🧪 Tests

Run all tests:

```bash
pytest test_solution.py
```

Run a specific test function:

```bash
# <test_function> = {test_is_trees_synchronized_returns_list, test_is_trees_synchronized}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 7}

pytest test_solution.py::test_is_trees_synchronized[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly implements the logic for checking if two binary trees are mirrors of each other.
- The use of recursion in `are_trees_equal` is appropriate for traversing the trees.
- The helper function `get_subtree_or_none` improves readability by abstracting away the dictionary key access.
- The code handles edge cases such as empty subtrees gracefully.
- The final return statement correctly provides the synchronization status and the root value of the first tree.