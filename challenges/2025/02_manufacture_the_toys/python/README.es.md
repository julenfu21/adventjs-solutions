<div align="center">
    <h1>Reto #2: 🏭 Fabrica los Juguetes — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #2 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #2](../README.es.md).


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
# <test_function> = {test_manufacture_gifts_returns_list, test_manufacture_gifts}

pytest test_solution.py::<test_function>
```

Ejecutar un test parametrizado individual:

```bash
# <index> = {0 - 4}

pytest test_solution.py::test_manufacture_gifts[gifts_to_produce<index>-expected_toys<index>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- ...