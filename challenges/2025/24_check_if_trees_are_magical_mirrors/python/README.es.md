<div align="center">
    <h1>Reto #24: 🪞 Verifica si los Árboles son Espejos Mágicos — Python</h1>
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

Esta carpeta contiene los **tests y soluciones** del Reto #24 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #24](../README.es.md).


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
# <función_de_test> = {test_is_trees_synchronized_returns_list, test_is_trees_synchronized}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 7}

pytest test_solution.py::test_is_trees_synchronized[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica para verificar la simetría de los árboles es correcta y maneja bien los casos de nodos nulos.
- El uso de funciones auxiliares anidadas (`get_subtree_or_none` y `are_trees_equal`) mejora la legibilidad y la modularidad.
- El código es eficiente y utiliza una recursión adecuada para recorrer los árboles.
- El formato del código es limpio y sigue las convenciones de Python.