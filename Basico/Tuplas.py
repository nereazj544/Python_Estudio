# TUPLAS = ()

my_tuple = tuple()  # Crea una tupla vacía
my_other_tuple = ()

my_tuple=(20, 1.53, "Neo", "Kurai")  # Crea una tupla con diferentes tipos de datos
print(type(my_tuple))  # Imprime el tipo de la tupla

print(my_tuple[2])
print(my_tuple[-1])

print(my_tuple.count("Neo"))  # Cuenta cuántas veces aparece "Neo" en la tupla
print(my_tuple.index("Neo"))  # Busca el índice del elemento "Neo" en la tupla

