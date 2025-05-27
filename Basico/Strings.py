print('Longitud de una cadena')

my_str = "Hola, Mundo!"
my_other_str = "mi otra cadena de texto"

print(f"Longitud de la cadena '{my_str}': {len(my_str)}")  # Imprime la longitud de la cadena

print(my_str + ", " + my_other_str)  # Concatena dos cadenas de texto

my_salto_line = "Esta es una nueva línea\ncon salto de línea"  # Crea una cadena con un salto de línea
print(my_salto_line)  # Imprime una cadena con un salto de línea


my_tab_line = "\tEsta es una nueva línea con tabulación"  # Crea una cadena con un tabulador
print(my_tab_line)  # Imprime una cadena con un tabulador

my_scape_str = "\\t Este es un String \\n escapado"
print(my_scape_str)  # Imprime una cadena con un salto de línea y un tabulador

# lenguage_ = 'P y t h o n'
        #      0 1 2 3 4 5
lenguage = 'Python'
a, b, c, d, e, f  = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

lenguage_slice = lenguage[2:5]  # Crea una subcadena desde el índice 2 hasta el 5 (sin incluir el 5)
print(lenguage_slice)

print(lenguage[2:])  # Crea una subcadena desde el índice 2 hasta el final
print(lenguage[:3])  # Crea una subcadena desde el inicio hasta el índice 3 (sin incluir el 3)
print(lenguage[::-1])  # Imprime la cadena en orden inverso


print(lenguage.capitalize()) # Convierte la primera letra de la cadena a mayúscula
print(lenguage.upper())  # Convierte la cadena a mayúsculas
print(lenguage.lower())  # Convierte la cadena a minúsculas
print(lenguage.title())  # Convierte la primera letra de cada palabra a mayúscula
print(lenguage.replace('P', 'p'))  # Reemplaza la letra 'P' por 'p' en la cadena
print(lenguage.startswith('P'))  # Verifica si la cadena comienza con 'P'
print(lenguage.endswith('n'))  # Verifica si la cadena termina con 'n'
print(lenguage.find('t'))  # Busca la letra 't' en la cadena y devuelve su índice
print(lenguage.index('t'))  # Busca la letra 't' en la cadena y devuelve su índice (lanza error si no se encuentra)
print(lenguage.count('o'))  # Cuenta cuántas veces aparece la letra 'o' en la cadena
print(lenguage.isnumeric()) # Verifica si la cadena contiene solo números (devuelve False)
print(lenguage.isalpha())  # Verifica si la cadena contiene solo letras
