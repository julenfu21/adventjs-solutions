<div align="center">
    <h1>Reto #1: 🎁 Filtrar los Regalos Defectuosos — Python</h1>
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

Esta carpeta contiene los **tests y soluciones** del Reto #1 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #1](../README.es.md).


## 📊 Detalles del Reto

| Dificultad | Puntuación |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Dificultad-FÁCIL-brightgreen" alt="Dificultad: Fácil" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuación-6%2F8-lightcoral" alt="Puntuación: 5-6" style="vertical-align: middle;"> |


## 💻 Solución

Ir a [`solution.py`](solution.py) para ver la implementación.


## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest test_solution.py
```

Ejecutar un test en específico:

```bash
# <función_de_test> = {test_filter_gifts_returns_list, test_filter_gifts}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 6}

pytest test_solution.py::test_filter_gifts[test-<index>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La solución es correcta y eficiente.
- El código es limpio, legible y sigue las convenciones de Python.
- Utiliza una comprensión de listas, que es una forma idiomática y concisa de resolver el problema.