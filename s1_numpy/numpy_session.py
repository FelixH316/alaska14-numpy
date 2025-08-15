# *********************************************************
# COURSE 14 SESSION 01
# *********************************************************
"""
HOW TO LOAD DATA: LOCAL VS REMOTE
"""
import numpy as np

URL1 = "https://gist.githubusercontent.com/ahcamachod/41b8a65c5e5b58125401deafb68af460/raw/f84320f69efa1cc3e86e1db054422cfa4869c63e/manzanas.csv"
URL2 =  "reference/manzanas.csv"

# 12 * 7 + 3 = 87 months
# np.arange(1, 88, 1)   # start (inc), stop (non-i), step
datos = np.loadtxt(URL1, delimiter=',', usecols=np.arange(1, 88, 1))

print(datos)
print(type(datos))


"""
ARRAYS ADVANTAGES

Las listas en Python son estructuras de datos básicas que pueden contener elementos de diferentes tipos (enteros, cadenas, otras listas, etc.). Por otro lado, Numpy (Numerical Python) es una biblioteca de Python que proporciona soporte para matrices multidimensionales, estructuras de datos más avanzadas y eficientes para cálculos numéricos.

Aquí tienes un ejemplo de cómo convertir una lista en un array Numpy:
"""
# import numpy as np
print("\n\n")

# crea una lista
lista = [1, 2, 3, 4, 5]

# convierte la lista en un array Numpy
array = np.array(lista)

print("Lista: ", lista)
print("Array: ", array)

# Salida
# Lista: [1, 2, 3, 4, 5]

# Array: [1 2 3 4 5]

"""
Existen varias ventajas en el uso de arrays Numpy en lugar de listas regulares de Python y aquí tienes algunas de ellas:

1. Eficiencia de procesamiento: Las operaciones matemáticas en los arrays Numpy son mucho más rápidas que en las listas regulares, ya que Numpy está optimizado para trabajar con conjuntos de datos homogéneos y libera memoria de la computadora de manera rápida.

2. Facilidad de uso: Las operaciones matemáticas en los arrays Numpy se expresan de manera mucho más clara y concisa que en las listas regulares, lo que hace que el código sea más fácil de leer y mantener.

3. Integración con otras bibliotecas: Numpy es una de las bibliotecas más utilizadas en ciencia de datos y aprendizaje automático. Muchas otras bibliotecas, como Pandas y Matplotlib, están diseñadas para trabajar directamente con arrays Numpy.

Comparación de rendimiento: listas vs arrays

Centrándonos en la eficiencia, podemos comparar el tiempo necesario para realizar un cálculo utilizando listas y arrays.
"""
print("\n\n")
# import numpy as np
import time

# crea una lista con 1000000 elementos
lista = list(range(1000000))

# convierte la lista en un array Numpy
array = np.array(lista)

# comienza a medir el tiempo para la operación con la lista
start_time = time.time()

# realiza la operación de elevar al cuadrado cada elemento de la lista
lista_cuadrado = [i**2 for i in lista]

# detiene el cronómetro
tiempo_lista = time.time() - start_time

# comienza a medir el tiempo para la operación con el array
start_time = time.time()

# realiza la operación de elevar al cuadrado cada elemento del array
array_cuadrado = array**2

# detiene el cronómetro
tiempo_array = time.time() - start_time

print("Tiempo de la operación con la lista: ", tiempo_lista)
print("Tiempo de la operación con el array: ", tiempo_array)

# Salida
# Tiempo de la operación con la lista: 0.2745847702026367

# Tiempo de la operación con el array: 0.004081010818481445

"""
Como se puede ver, la operación realizada con el array Numpy fue mucho más rápida que con la lista regular, lo que demuestra la eficiencia en el procesamiento con el array.
"""

