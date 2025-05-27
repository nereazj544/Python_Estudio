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