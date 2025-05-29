# Excepciones

num1, num2 = int(10), 9
# num2 = "5"  # Cambiamos num2 a una cadena para provocar un error


# try:
#     print(num1 + num2)  # Intento de sumar un entero y una cadena
# except TypeError as e:
#     print("> se ha producido un error de tipo al intentar sumar un entero y una cadena.")
#     print(f">Más contenido: eror: {e}")


try:
    print(num1 + num2)  # Intento de sumar un entero y una cadena
except:
    print("> se ha producido un error al intentar sumar")

else:
    print("> La suma se realizó correctamente, no hubo errores.")
finally:
    print("> Este bloque se ejecuta siempre, independientemente de si hubo un error o no.")
    
