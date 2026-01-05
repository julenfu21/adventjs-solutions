<div align="center">
    <h1>Reto #17: 🎄 El Panel de Luces Navideñas — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #17 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #17](../README.es.md).


## 📊 Detalles del Reto

| Dificultad | Puntuación |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Dificultad-FÁCIL-brightgreen" alt="Dificultad: Fácil" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuación-7%2F8-blueviolet" alt="Puntuación: 7-8" style="vertical-align: middle;"> |


## 💻 Solución

Ir a [`solution.py`](solution.py) para ver la implementación.


## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest test_solution.py
```

Ejecutar un test en específico:

```bash
# <función_de_test> = {test_has_four_lights_returns_boolean, test_has_four_lights}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 8}

pytest test_solution.py::test_has_four_lights[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- El código es correcto y maneja eficientemente la búsqueda de líneas de 4 luces.
- La lógica para verificar filas horizontales y verticales es clara y concisa.
- El uso de `all()` es una forma eficiente de verificar las condiciones.
- El código está bien formateado y es fácil de leer.