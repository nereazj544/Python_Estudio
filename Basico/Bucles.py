## Bucles ##

# Bucle for
for i in range(10):
    print(i)


# Bucle while
i = 0
while i < 10:
    print(i)
    i += 1


# Bucle for con lista
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)


# Bucle for con cadena
my_string = "Hola"
for char in my_string:
    print(char)



# Bucle for con diccionario
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Clave: {key}, Valor: {value}")


# Bucle for con enumerate
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(f"Índice: {index}, Valor: {value}")


my_condition =0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se ha alcanzado el valor 15, saliendo del bucle.")
        break

    print(f"Valor actual: {my_condition}")