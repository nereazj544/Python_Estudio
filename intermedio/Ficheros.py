## FICHEROS

import os

# .txt

text_file = open("intermedio/doc/my_file2.txt", "w") # Crear un fichero
text_file_read = open("intermedio/doc/my_file.txt", "r") # Abrir un fichero para leer
#print(text_file_read.read()) # Leer el fichero
#print(text_file_read.read(10)) # Leer los primeros 10 caracteres del fichero
# print(text_file_read.readline()) # Leer la primera línea del fichero
# print(text_file_read.readlines()) # Leer todas las líneas del fichero

for line in text_file_read.readlines():
    print(line.strip())  # Imprimir cada línea sin saltos de línea

text_file.write("Hola mundo\n")

os.remove("intermedio/doc/my_file2.txt")  
# Eliminar el fichero creado


"""
- r+ > leer y escribir
- w+ > leer y escribir. Si el fichero no existe lo crea, en caso que exista elimina su contenido
- r > leer
- w > escribir, eleminando antes el contenido del fichero (si existe)
- a > escribir, añadiendo el nuevo contenido al final del fichero
"""