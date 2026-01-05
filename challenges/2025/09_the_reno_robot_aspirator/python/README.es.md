<div align="center">
    <h1>Reto #9: 🦌 El Reno Robot Aspirador — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #9 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #9](../README.es.md).


## 📊 Detalles del Reto

| Dificultad | Puntuación |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Dificultad-DIFÍCIL-red" alt="Dificultad: Difícil" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> |


## 💻 Solución

Ir a [`solution.py`](solution.py) para ver la implementación.


## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest test_solution.py
```

Ejecutar un test en específico:

```bash
# <función_de_test> = {test_move_reno_returns_string, test_move_reno}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 9}

pytest test_solution.py::test_move_reno[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica para encontrar la posición inicial del reno es clara.
- El manejo de los movimientos y la actualización de la posición son correctos.
- La detección de colisiones ('crash') y recolección ('success') está bien implementada.
- El código maneja correctamente los casos de borde como salirse del tablero.
- El uso de un diccionario para `reindeer_location` es legible.


### ⚠️ Puntos a Mejorar

- La condición para verificar si el reno está dentro del tablero podría ser un poco más concisa.


### 🧭 Próximos Pasos

- Considerar refactorizar la condición `if not (0 <= current_row_id < len(clean_board) and 0 <= current_column_id < len(clean_board[current_row_id])):` para mejorar la legibilidad, quizás dividiéndola en dos comprobaciones separadas o usando variables intermedias si se considera necesario.