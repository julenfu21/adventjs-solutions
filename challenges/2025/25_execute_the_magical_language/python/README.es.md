<div align="center">
    <h1>Reto #25: 🪄 Ejecuta el Lenguaje Mágico — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #25 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #25](../README.es.md).


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
# <función_de_test> = {test_execute_returns_int, test_execute}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 13}

pytest test_solution.py::test_execute[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La estructura del código es modular y utiliza funciones auxiliares para procesar bucles y condicionales, lo que mejora la legibilidad.
- La lógica para manejar los bucles y condicionales parece correcta, incluyendo el manejo de los saltos de instrucción.
- El uso de tipos (`Literal`) para `expression_end_symbol` es una buena práctica.


### ⚠️ Puntos a Mejorar

- La función `get_scope_of_special_expression` asume que el símbolo de fin siempre se encontrará, lo que podría causar un error si la expresión está mal formada (por ejemplo, un `{` sin un `}`).
- La recursión implícita a través de `process_expression` llamando a `process_conditional_expression` y `process_loop_expression`, y estas a su vez a `process_expression`, podría llevar a un desbordamiento de pila para programas muy anidados (aunque el problema especifica que no hay anidamiento de dos bucles o dos condicionales, la estructura general podría ser un problema en otros contextos).


### 🧭 Próximos Pasos

- Implementar manejo de errores en `get_scope_of_special_expression` para el caso en que no se encuentre el símbolo de fin de expresión.
- Considerar una implementación iterativa con una pila explícita para el manejo de bucles y condicionales si se anticipa la posibilidad de anidamiento profundo en futuras versiones del lenguaje.