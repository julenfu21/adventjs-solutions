<div align="center">
    <h1>Reto #22: 🎄 El Laberinto del Trineo — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #22 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #22](../README.es.md).


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
# <función_de_test> = {test_can_escape_returns_boolean, test_can_escape}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 8}

pytest test_solution.py::test_can_escape[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La implementación utiliza una búsqueda en anchura (BFS) de manera efectiva para resolver el problema del laberinto.
- El código está bien estructurado con funciones auxiliares claras para la obtención de la posición inicial, la validación de coordenadas y la obtención de vecinos.
- El uso de `dataclass` para `Square` mejora la legibilidad y la inmutabilidad de las coordenadas.
- El manejo de `visited` y la cola (`deque`) es correcto para un algoritmo BFS.


### ⚠️ Puntos a Mejorar

- La complejidad ciclomática es alta (24), lo que indica un flujo de control potencialmente complejo. Aunque las funciones auxiliares ayudan a modularizar, el bucle principal y las condiciones internas contribuyen a esta métrica.


### 🧭 Próximos Pasos

- Considerar refactorizar el bucle principal del BFS para simplificar el flujo de control y reducir la complejidad ciclomática, si es posible sin sacrificar la claridad.