## Condicionales
print("True o False")
input_value = input("Escribe True o False: ")



if input_value == "True" or input_value == "true":
    print("La condición es verdadera")
elif input_value == "False" or input_value == "false":
    print("La condición es falsa")
else:
    print("La condición es desconocida")

input_value_temp = input("Escribe una temperatura: ")

if input_value_temp > "0":
    print(f"la temperatura es positiva:{input_value_temp}")
elif input_value_temp < "0":
    print(f"la temperatura es negativa:{input_value_temp}")
else:
    print(f"la temperatura es cero:{input_value_temp}")




my_string = "Hola Mundo"
my_string_empty = ""

# Por defecto los if son True 

print("my_string, comparacion con if")
if my_string: # Si la cadena no está vacía, se evalúa como True
    print("La cadena no está vacía")
else:
    print("La cadena está vacía")

print("my_string_empty, comparacion con if")
if my_string_empty:
    print("La cadena no está vacía")
else:
    print("La cadena está vacía")