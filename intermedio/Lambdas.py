# Lambdas
# Definicion de lambdas
# Las funciones lambda son funciones anónimas que se definen en una sola línea.
# Se utilizan principalmente para operaciones simples y se pueden pasar como argumentos a otras funciones.
# Son útiles cuando se necesita una función pequeña y no se quiere definir una función completa con def.


# lambda fist, second: fist + second
sum = lambda first, second: first + second  # Definición de una función lambda que suma dos números

print(sum(5, 13))  # Llamada a la función lambda con argumentos 5 y 13

print((lambda first, second: first + second)(5, 10))  # Llamada a la función lambda

