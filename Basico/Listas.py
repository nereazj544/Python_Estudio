## Listas = []

my_list = list () # si no se especifica 'list' sera una tupla
my_list = [1, 2, 3, 4, 5]  # Crea una lista de números
print("Lista original:", my_list)  # Imprime la lista original

my_list_str = ["hola"]
print("Lista de cadenas:", my_list_str)  # Imprime la lista de cadenas
my_list_str.append("mundo")  # Agrega un nuevo elemento a la lista de cadenas
print("Lista de cadenas después de agregar un elemento:", my_list_str)  # Imprime la lista de cadenas después de agregar un elemento

                # 0    1    2       3              
my_other_list = [20, 1.53, "Neo", "Kurai"]
print("Otra lista con diferentes tipos de datos:", my_other_list)  # Imprime otra lista con diferentes tipos de datos

print(len(my_other_list))  # Imprime la longitud de la lista con diferentes tipos de datos

print(my_other_list[0])  # Imprime el primer elemento de la lista
print(my_other_list[1])  # Imprime el segundo elemento de la lista

print(my_other_list[-1])
print(my_other_list[-2])  # Imprime el penúltimo elemento de la lista

print(my_other_list.count("Neo"))  # Cuenta cuántas veces aparece "Neo" en la lista
print(my_other_list.index("Neo"))  # Busca el índice del elemento "Neo" en la lista

# El nombre da igual, simplemente son nombres de variables que se colocan para mostrar el concepto de la lista
age, height, name, surname = my_other_list  # Desempaqueta la lista en variables
print(name)

print(list([1, 2]))
print([1, 2, "Neo"])


# Opciones para crear listas
my_list = list("Hola Mundo")  # Convierte una cadena en una lista de caracteres
my_list = [1, 2, 3, 4, 5]  # Crea una lista de números
print("Lista de numeros, usado POP")
print(my_list.pop()) # Elimina y devuelve el último elemento de la lista
print("Lista de numeros, despues de usar POP")
print(my_list)  # Imprime la lista después de eliminar el último elemento

print("Lista de numeros, usado POP con indice")
print(my_list.pop(2))  # Elimina y devuelve el tercer elemento de la lista
print(my_list)  # Imprime la lista después de eliminar el último elemento