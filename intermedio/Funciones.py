#funciones de orden superior
# Las funciones de orden superior son aquellas que pueden recibir otras funciones como argumentos o devolverlas como resultado.
# Estas funciones son útiles para crear código más modular y reutilizable.



def sum_value(first, second):
    return first + second + 1  # Definición de una función que suma dos números

# funcion de orden superior
def sum_one (value):
    return value + 1  # Definición de una función que suma 1 a un valor

def sum_values (first, second):
    return sum_one(first + second)  # Llamada a la función pasada como argumento

print(sum_values(5, 10))  # Llamada a la función que suma dos números y luego aplica sum_one

## Closures ##
# Un closure es una función que recuerda el entorno en el que fue creada, incluso después de que ese entorno haya sido destruido.

def ten ():
    def add(value):
        return value + 10
    return add  # Devuelve la función add, que es un closure

print(ten()(3))  # Llamada al closure con el valor 3, que devuelve 13
add_ten = ten()  # Llama a la función ten y obtiene el closure add
print(add_ten(5))  # Llamada al closure con el valor 5, que devuelve 15