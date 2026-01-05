<div align="center">
    <h1>Challenge #25: 🪄 Execute the Magical Language — Python</h1>
</div>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 📖 Overview

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #25. Refer to the [main README of Challenge #25](../README.md) for more detailed instructions.


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
# <test_function> = {test_execute_returns_int, test_execute}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 13}

pytest test_solution.py::test_execute[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly implements the logic for the given programming language.
- The use of helper functions for processing conditionals and loops improves readability.
- The code handles nested structures as described in the problem statement.


### ⚠️ Weak Points

- The `get_scope_of_special_expression` function has a potential bug: it assumes the `expression_end_symbol` will always be found and does not handle cases where it might be missing or if the `expression_end_index` goes out of bounds.
- The `process_loop_expression` function has a potential infinite loop if the `current_value` never becomes 0 within the loop, as it does not have a mechanism to break out if the loop body doesn't modify `current_value` in a way that leads to termination.


### 🧭 Next Steps

- Add error handling to `get_scope_of_special_expression` to gracefully handle missing closing symbols.
- Consider adding a safeguard or a maximum iteration count to `process_loop_expression` to prevent potential infinite loops in edge cases, although the problem statement implies valid inputs.