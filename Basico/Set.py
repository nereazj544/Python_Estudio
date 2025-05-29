## SETS

my_set = set()  # Crea un conjunto vacío
my_set_ = {} # esto seria un diccionario.
my_other_set = {1, 2, 3, 4, 5}  # Crea un conjunto de números

print(type(my_other_set))  # Imprime el tipo del otro conjunto
print(type(my_set))  # Imprime el tipo del conjunto
print(type(my_set_))  # Imprime el tipo del conjunto

print(len(my_other_set))  # Imprime la longitud del conjunto de números

my_other_set.add("Neo")
print(my_other_set)  # Imprime el conjunto después de agregar un elemento
# my_other_set.add("Neo") # Esto no agregara un nuevo elemento, ya que "Neo" ya existe en el conjunto

my_other_set.remove("Neo")  # Elimina un elemento del conjunto
print(my_other_set)  # Imprime el conjunto después de eliminar un elemento
my_other_set.discard("Neo")  # Intenta eliminar un elemento que no existe, no genera error
print(my_other_set)  # Imprime el conjunto después de intentar eliminar un elemento que no existe
my_other_set.clear()  # Limpia el conjunto, eliminando todos sus elementos
print(my_other_set)  # Imprime el conjunto después de limpiarlo
