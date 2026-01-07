<div align="center">
    <h1>Reto #5: ⏱️ La Cuenta Atrás para el Despegue — Python</h1>
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

Esta carpeta contiene los **tests y soluciones** del Reto #5 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #5](../README.es.md).


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
# <función_de_test> = {test_time_until_take_off_returns_int, test_time_until_take_off}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 8}

pytest test_solution.py::test_time_until_take_off[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- El código es correcto y maneja adecuadamente la conversión de formatos de fecha y la diferencia de tiempo.
-  La lógica para calcular la diferencia en segundos es clara y eficiente.
-  El uso de `datetime.strptime` y `total_seconds()` es apropiado para la tarea.
-  El código es limpio, legible y sigue las convenciones de Python.