# 🗺️ Taller 2: Operaciones con Listas en Python (Países)

¡Hola! Este es mi repositorio con la solución al segundo taller de laboratorio de Algoritmos 1, enfocado en aprender a crear, modificar, eliminar y consultar información usando listas.

El programa aplica diferentes métodos de Python sobre una lista base con 5 países de Sudamérica para resolver cada punto de la guía.

## 📌 ¿Cómo funciona el código?

El taller está dividido en archivos independientes para que cada ejercicio se pueda probar por separado de forma limpia:

1. **1Creacion_de_lista.py:** Crea la lista con los 5 países iniciales, la muestra completa y luego imprime solo el primero y el último.
2. **2Acceder_a_posiciones.py:** Busca un país por su posición exacta e intenta forzar un error con un índice que no existe para explicar el comportamiento.
3. **3Agregar_elementos.py:** Agrega un país nuevo al final de la lista y mete otro en una posición específica del medio.
4. **4Eliminar_elementos.py:** Borra países usando diferentes métodos: por su nombre, borrando el último o sacándolo por su posición.
5. **5Modificar_elementos.py:** Cambia el nombre de un país por otro y muestra cómo se veía la lista antes y después del cambio.
6. **6Agregar_multiples_elementos.py:** Mete varios países de golpe al final de la lista y te dice cuántos elementos quedaron en total.

## 🛠️ Reglas del taller que se cumplieron:

* **Estructura limpia:** Cada punto se separó en un archivo diferente para que no se mezclen las operaciones en la consola.
* **Manejo de errores:** En el punto 2 se documentó y explicó el error `IndexError` que arroja Python cuando buscas una posición que no existe.
* **Uso de métodos oficiales:** Se usaron las funciones nativas de Python como `.append()`, `.insert()`, `.remove()`, `.pop()`, `.extend()` y `len()` sin inventar lógicas raras.

## 🚀 Cómo ejecutar los ejercicios

Cualquiera de los archivos se puede probar por separado ejecutándolo desde la terminal de VS Code. Por ejemplo, para correr el segundo punto:

```bash
python 2Acceder_a_posiciones.py