<div align="center">
    <h1>Reto #16: 🎁 Empaquetando Regalos para Santa — Python</h1>
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

Esta carpeta contiene los **tests y soluciones** del Reto #16 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #16](../README.es.md).


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
# <función_de_test> = {test_pack_gifts_returns_int, test_pack_gifts}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 12}

pytest test_solution.py::test_pack_gifts[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica para calcular el número mínimo de trineos es correcta y eficiente.
- El código maneja correctamente los casos de borde, como una lista de regalos vacía o regalos que exceden el peso máximo del trineo.
- El uso de variables descriptivas mejora la legibilidad.
- El flujo de control es claro y fácil de seguir.