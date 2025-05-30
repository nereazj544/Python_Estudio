## FICHEROS

import os

# .txt

text_file = open("intermedio/doc/my_file2.txt", "w") # Crear un fichero
text_file_read = open("intermedio/doc/my_file.txt", "r") # Abrir un fichero para leer
print(text_file_read.read()) # Leer el fichero

"""
- r+ > leer y escribir
- w+ > leer y escribir. Si el fichero no existe lo crea, en caso que exista elimina su contenido
- r > leer
- w > escribir, eleminando antes el contenido del fichero (si existe)
- a > escribir, añadiendo el nuevo contenido al final del fichero
"""