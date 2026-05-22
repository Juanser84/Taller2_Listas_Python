# Actividad 1: Crear una lista  

# Creación de una lista con 5 países de Sudamérica

list = ['colombia', 'ecuador', 'peru', 'venezuela', 'chile']

# Imprimir cada país de la lista utilizando su índice

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

# imprime unicamente el primer y ultimo país de la lista

# print(list[0])
# print(list[4])

# fin de la actividad 1

#--------------------------------------------------------------------------

# Actividad 2: Acceder a posiciones específicas de la lista

# Acceder a posiciones específicas de la lista

# Imprimir el pais ubicado en la posición 2

# print(list[2])

# Intente acceder a una posición que no existe en la lista

# print(list[5])

# Explique el error que se produce al intentar acceder a una posición que no existe en la lista

# El error que se produce es un IndexError, que indica que el índice que se está intentando acceder está fuera del rango de la lista. En este caso, la lista tiene 5 elementos, por lo que los índices válidos son del 0 al 4. Al intentar acceder al índice 5, se produce el error porque no existe un elemento en esa posición.

# fin de la actividad 2

#--------------------------------------------------------------------------

# Actividad 3: Agregar elementos a la lista

# Agregar un elemento al final de la lista

list.append('argentina')

# Agregar un elemento en una posición específica de la lista

list.insert(2, 'brasil')

# Muestre el resultado de la lista despues de cada una de las operaciones anteriores

print(list)

# fin de la actividad 3

#--------------------------------------------------------------------------

