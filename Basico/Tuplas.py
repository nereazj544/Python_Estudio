# TUPLAS = ()

my_tuple = tuple()  # Crea una tupla vacía
my_other_tuple = (2, 13, 290)

my_tuple=(20, 1.53, "Neo", "Kurai")  # Crea una tupla con diferentes tipos de datos
print(type(my_tuple))  # Imprime el tipo de la tupla

print(my_tuple[2])
print(my_tuple[-1])

print(my_tuple.count("Neo"))  # Cuenta cuántas veces aparece "Neo" en la tupla
print(my_tuple.index("Neo"))  # Busca el índice del elemento "Neo" en la tupla

sum_tuple = my_other_tuple + my_tuple
print(sum_tuple)
print(sum_tuple[5:7])

# Convertir una tupla a mutable lista
my_list = list(my_tuple)
print(type(my_list))  # Convierte la tupla a una lista y la imprime


my_list.insert(0, "Kurai")
print(my_list)  # Imprime la lista después de modificarla
my_tuple = tuple(my_list)
print(my_tuple)  # Convierte la lista de nuevo a tupla y la imprime
print(type(my_tuple))  # Imprime el tipo de la tupla después de la conversión

# del my_tuple  # Elimina la variable
