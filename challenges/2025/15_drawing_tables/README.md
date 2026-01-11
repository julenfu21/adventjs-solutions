<div align="center">
    <h1>Challenge #15: ✏️ Drawing Tables</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-MEDIUM-yellow" alt="Difficulty: Medium">
</p>
<br>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish" style="margin-right:16px;">
    </a>
    <a href="README.eu.md">
        <img src="https://img.shields.io/badge/Language-eu-green.svg" alt="Basque">
    </a>
</p>


## 💻 Implementations & Scores

| Language | Score | Implementation |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-6%2F8-lightcoral" alt="Score: 5-6" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

**ChatGPT has arrived at the North Pole** and the elf *Sam Elfman* is working on a gift and children management application.

To improve the presentation, he wants to create a `drawTable` function that receives an **array of objects** and turns it into a **text table**.

The drawn table must have:

- A header with column letters (`A`, `B`, `C`…).
- The content of the table is the values of the objects.
- The values must be left-aligned.
- The fields always leave one space on the left.
- The fields leave on the right the space needed to align the box.

The function receives a second parameter `sortBy` that indicates the name of the field by which the **rows must be sorted**. The order will be **ascending alphabetical** if the values are strings and **ascending numeric** if they are numbers.

Check the example to see how you should draw the table:


## 💡 Examples

```js
drawTable(
  [
    { name: 'Charlie', city: 'New York' },
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' }
  ],
  'name'
)
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

drawTable(
  [
    { gift: 'Book', quantity: 5 },
    { gift: 'Music CD', quantity: 1 },
    { gift: 'Doll', quantity: 10 }
  ],
  'quantity'
)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
```