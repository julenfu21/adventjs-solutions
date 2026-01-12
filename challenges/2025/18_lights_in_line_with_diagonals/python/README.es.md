<div align="center">
    <h1>Reto #18: 🎄 Luces en Línea con Diagonales — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés" style="margin-right:16px;">
    </a>
    <a href="README.eu.md">
        <img src="https://img.shields.io/badge/Idioma-eu-green.svg" alt="Euskera">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #18 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #18](../README.es.md).


## 📊 Detalles del Reto

| Dificultad | Puntuación |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Dificultad-MEDIO-yellow" alt="Dificultad: Medio" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuación-8%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> |


## 💻 Solución

Ir a [`solution.py`](solution.py) para ver la implementación.


## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest test_solution.py
```

Ejecutar un test en específico:

```bash
# <función_de_test> = {test_has_four_in_a_row_returns_boolean, test_has_four_in_a_row}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 6}

pytest test_solution.py::test_has_four_in_a_row[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica para detectar líneas horizontales, verticales y diagonales es correcta y cubre los casos necesarios.
- El uso de funciones auxiliares para cada tipo de línea mejora la legibilidad del código principal.
- El código maneja correctamente los límites del tablero para evitar errores de índice.
- La estructura general del código es clara y fácil de seguir.