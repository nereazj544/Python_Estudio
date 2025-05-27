# Variables
print("Variables")

my_var_str = "Hola, Mundo!"  # Variable de tipo cadena de texto
print(my_var_str)  # Imprime el valor de la variable

my_var_int = 42  # Variable de tipo entero
print(my_var_int)  # Imprime el valor de la variable

name = "Neo"
ciudad = 'Oviedo'
is_student = True  # Variable de tipo booleano

skills = ['C#', 'Python', 'Typescript']  # Variable de tipo lista

print(f"Nombre: {name}, Ciudad: {ciudad}, Estudiante: {is_student}")  # Imprime los valores de las variables

skills.append('CSS') # Agrega un nuevo elemento a la lista de habilidades
skills.append('HTML') # Agrega un nuevo elemento a la lista de habilidades

print(f"Skills: {', '.join(skills)}")  # Imprime los valores de la lista de habilidades


print("\nMultiple:")
# Declaracion multiple
_name, _ciudad, _is_student = "Neo", "Oviedo", True  # Declaración múltiple de variables
print(f"Nombre: {_name}, Ciudad: {_ciudad}, Estudiante: {_is_student}")  # Imprime los valores de las variables