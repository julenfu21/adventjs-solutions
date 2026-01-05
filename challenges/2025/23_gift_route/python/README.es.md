<div align="center">
    <h1>Reto #23: 🎁 Ruta de Regalos — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #23 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #23](../README.es.md).


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
# <función_de_test> = {test_min_steps_to_deliver_returns_int, test_min_steps_to_deliver}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 6}

pytest test_solution.py::test_min_steps_to_deliver[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica general para encontrar la distancia mínima usando BFS es correcta.
- Las funciones auxiliares para obtener la posición inicial, las casas y los vecinos son claras y bien definidas.
- El manejo de coordenadas inválidas y obstáculos es adecuado.


### ⚠️ Puntos a Mejorar

- El algoritmo BFS actual no calcula la distancia a cada casa de forma independiente. Intenta visitar todas las casas en una sola pasada del BFS, lo que no es correcto para el requisito de 'vuelve inmediatamente a S'.
- La lógica de `remaining_houses` y la condición `while queue and remaining_houses >= 0` no manejan correctamente el caso en que una casa sea inalcanzable después de haber encontrado otras.



### 🧭 Próximos Pasos

- Modificar el algoritmo para que calcule la distancia mínima a cada casa `'G'` de forma independiente. Esto implica ejecutar un BFS separado para cada casa o adaptar el BFS para que registre las distancias a cada casa encontrada.
- Asegurarse de que si alguna casa `'G'` es inalcanzable, la función devuelva `-1`. Esto puede requerir verificar si todas las casas fueron alcanzadas después de cada BFS individual.