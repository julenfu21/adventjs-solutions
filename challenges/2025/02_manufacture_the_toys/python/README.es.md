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
# <función_de_test> = {test_manufacture_gifts_returns_list, test_manufacture_gifts}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 6}

pytest test_solution.py::test_manufacture_gifts[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- El código es correcto y maneja los casos de borde especificados (cantidades no válidas).
- La lógica es clara y fácil de seguir.
- Utiliza estructuras de datos apropiadas y eficientes para la tarea.
- El código es limpio, legible y sigue las convenciones de estilo de Python.