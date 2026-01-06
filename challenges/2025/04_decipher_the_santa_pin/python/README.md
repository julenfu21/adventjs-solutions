<div align="center">
    <h1>Challenge #4: 🧮 Decipher the Santa PIN — Python</h1>
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

This folder contains the <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python solution and tests** for Challenge #4. Refer to the [main README of Challenge #4](../README.md) for more detailed instructions.


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
# <test_function> = {test_decode_santa_pin_returns_string, test_decode_santa_pin}

pytest test_solution.py::<test_function>
```

Run an individual parametrized test case:

```bash
# <index> = {2 - 8}

pytest test_solution.py::test_decode_santa_pin[test-<index>]
```


## 🧠 Code Review


### ✅ Strengths

- The code correctly parses the input string and deciphers the PIN.
- The `process_block` helper function is well-defined and handles operations correctly.
- Mod 10 arithmetic is correctly implemented for digit wrapping.
- Edge case of fewer than 4 digits is handled by returning null.
- Variable names are generally descriptive.


### ⚠️ Weak Points

- The `process_block` function raises a `ValueError` for the '<' operation when `last_digit` is `None`. This exception is not caught by the main function, which could lead to a program crash if the input starts with '[<]'.
- The main loop iterates character by character, which is less efficient than using regular expressions or string splitting to identify blocks.


### 🧭 Next Steps

-  Add error handling to catch the `ValueError` in `process_block` and return `None` or an appropriate indicator if the '<' operation is used without a preceding digit.
- Consider refactoring the block parsing logic to be more efficient, perhaps by using regular expressions to extract blocks directly.