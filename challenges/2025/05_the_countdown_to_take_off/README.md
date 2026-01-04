<div align="center">
    <h1>Challenge #5: ⏱️ The Countdown to Take Off</h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Difficulty-EASY-brightgreen" alt="Difficulty: Easy">
</p>
<br>


## 🌐 Read in Other Languages

<p align="center">
    <a href="README.es.md">
        <img src="https://img.shields.io/badge/Language-es-yellow.svg" alt="Spanish">
    </a>
</p>


## 💻 Implementations & Scores

| Language | Score | Implementation |
|:--------:|:-----:|----------------|
| <img src="../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> Python | <img src="https://img.shields.io/badge/Score-7%2F8-blueviolet" alt="Score: 7-8" style="vertical-align: middle;"> | [Go to Implementation](python/README.md) |


## 🎯 Instructions

Elves have a **secret timestamp**: it’s the exact date and time when **Santa Claus takes off with the sleigh** 🛷 to deliver gifts around the world. But at the North Pole they use a super weird format to store the time: `YYYY*MM*DD@HH|mm|ss NP` (example: `2025*12*25@00|00|00 NP`).

Your mission is to write a function that receives:

- `fromTime` → reference date in elf format (`YYYY*MM*DD@HH|mm|ss NP`).
- `takeOffTime` → the same takeoff date, also in elf format.

The function must return:

- The **full seconds** remaining until takeoff.
- If we’re exactly at takeoff time → `0`.
- If takeoff already happened → a **negative number** indicating how many seconds have passed since then.


## 📜 Rules

- First convert the elf format to a timestamp. The `NP` suffix indicates official North Pole time (no time zones or DST), so you can treat it as if it were UTC.
- Use differences in **seconds**, not milliseconds.
- Always round down (`floor`): only full seconds.


## 💡 Examples

```js
const takeoff = '2025*12*25@00|00|00 NP'

// from December 24, 2025, 23:59:30, 30 seconds before takeoff
timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)
// 30

// exactly at takeoff time
timeUntilTakeOff('2025*12*25@00|00|00 NP', takeoff)
// 0

// 12 seconds after takeoff
timeUntilTakeOff('2025*12*25@00|00|12 NP', takeoff)
// -12
```