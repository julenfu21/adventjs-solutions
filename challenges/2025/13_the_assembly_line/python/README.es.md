<div align="center">
    <h1>Reto #13: 🏭 La Cadena de Montaje — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #13 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #13](../README.es.md).


## 📊 Detalles del Reto

| Dificultad | Puntuación |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Dificultad-MEDIO-yellow" alt="Dificultad: Medio" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> |


## 💻 Solución

Ir a [`solution.py`](solution.py) para ver la implementación.


## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest test_solution.py
```

Ejecutar un test en específico:

```bash
# <función_de_test> = {test_run_factory_returns_string, test_run_factory}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 11}

pytest test_solution.py::test_run_factory[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica para simular el recorrido de la fábrica es correcta y maneja los tres casos de salida ('completed', 'loop', 'broken').
- El uso de `dataclass` para `Location` y `set` para `explored_locations` es eficiente y apropiado.
- La separación de la lógica en funciones auxiliares (`is_out_of_bounds`, `get_next_move`, `update_present_location`, `get_location_state`) mejora la legibilidad y modularidad.
- El código es limpio, bien formateado y utiliza nombres descriptivos para variables y funciones.