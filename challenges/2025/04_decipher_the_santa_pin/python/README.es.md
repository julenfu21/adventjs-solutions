<div align="center">
    <h1>Reto #4: 🧮 Descifra el PIN de Santa — Python</h1>
</div>


## 🌐 Leer en Otros Idiomas

<p align="center">
    <a href="README.md">
        <img src="https://img.shields.io/badge/Idioma-en-red.svg" alt="Inglés">
    </a>
</p>


## 📖 Información General

Esta carpeta contiene los **tests y soluciones** del Reto #4 en <img src="../../../../assets/python-logo.png" alt="Python" width="20" style="vertical-align: middle;"> **Python**. Para instrucciones más detalladas ir al [README principal del Reto #4](../README.es.md).


## 📊 Detalles del Reto

| Dificultad | Puntuación |
|:----------:|:-----:|
| <img src="https://img.shields.io/badge/Dificultad-MEDIO-yellow" alt="Dificultad: Medio" style="vertical-align: middle;"> | <img src="https://img.shields.io/badge/Puntuación-6%2F8-lightcoral" alt="Puntuación: 5-6" style="vertical-align: middle;"> |


## 💻 Solución

Ir a [`solution.py`](solution.py) para ver la implementación.


## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest test_solution.py
```

Ejecutar un test en específico:

```bash
# <función_de_test> = {test_decode_santa_pin_returns_string, test_decode_santa_pin}

pytest test_solution.py::<función_de_test>
```

Ejecutar un test parametrizado individual:

```bash
# <índice> = {2 - 8}

pytest test_solution.py::test_decode_santa_pin[test-<índice>]
```


## 🧠 Revisión de Código


### ✅ Puntos Fuertes

- La lógica para procesar los bloques y las operaciones es correcta.
- El manejo de la aritmética modular para los dígitos es adecuado.
- El código es legible y utiliza nombres descriptivos para variables y la función interna.
- La función interna `process_block` está bien definida y encapsula la lógica de procesamiento de un solo bloque.


### ⚠️ Puntos a Mejorar

- El uso de `ValueError` dentro de la función interna `process_block` para manejar el caso de `[<]` sin un dígito previo no es ideal, ya que la función principal espera un string o `None`. Esto podría manejarse de forma más integrada en el flujo principal.
- La variable `globals` detectada indica una posible variable global o un uso que podría ser refactorizado para mejorar la encapsulación y mantenibilidad.


### 🧭 Próximos Pasos

- Refactorizar el manejo del caso `[<]` sin dígito previo para que no lance una excepción, sino que se maneje dentro del bucle principal o devuelva un valor que el bucle principal pueda interpretar como un error o un estado inválido.
- Revisar el uso de variables globales para asegurar que no haya efectos secundarios no deseados y que la función sea puramente algorítmica.