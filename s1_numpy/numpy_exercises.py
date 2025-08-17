"""
# *********************************************************
# COURSE 14 EXERCISES 01
# *********************************************************

# HW 01 - Haga lo que hicimos

Ha llegado el momento de poner a prueba los conocimientos adquiridos
    durante la lección. Para ello, vamos a utilizar otro conjunto de
    datos en un desafío que se desarrollará a lo largo del curso. Este
    conjunto de datos es una versión modificada del archivo disponible
    en el sitio de Kaggle. Por lo tanto, utilizaremos el archivo raw
    disponible en Github.

*Enlace original:
    https://www.kaggle.com/datasets/joshmcadams/oranges-vs-grapefruit

*Archivo raw:
    https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv

En esta etapa, debes cargar los datos. Para hacerlo, importa NumPy y
    utiliza la función loadtxt. Utiliza el enlace de la URL y el
    parámetro usecols para omitir la primera columna. Puedes usar
    np.arange para crear la secuencia de números que representan las
    columnas. Por último, también es necesario incluir el parámetro
    skiprows=1 para que la primera línea de texto se omita al leer el
    archivo.
"""
import numpy as np

url = "https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv"

raw_data = np.loadtxt(url, delimiter=',', skiprows=1, usecols=np.arange(1, 6, 1))
print(raw_data)
