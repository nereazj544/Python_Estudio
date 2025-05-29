>(!NOTE)
> Python no tiene arrays como tal, pero las listas y tuplas pueden ser utilizadas como tales.

# Lista
- Son colecciones ordenadas y mutables de elementos. 
- Se definen con corchetes `[]`.
- Permite agregar, eliminar y modificar elementos.

# Tupla
- Son colecciones ordenadas e inmutables de elementos.
- Se definen con paréntesis `()`.
- No se pueden modificar una vez creadas, pero se pueden concatenar o repetir.


La principal diferencia entre una lista y una tupla es que las listas son mutables (pueden cambiar) y las tuplas son inmutables (no pueden cambiar una vez creadas).

Se pueden cambiar los tipos de las listas y tuplas.

```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list = list(my_tuple)
my_tuple = tuple(my_list)
```

# Set
- Son colecciones no ordenadas y mutables de elementos únicos.
- Se definen con llaves `{}` o con la función `set()`.
- No permiten elementos duplicados y no tienen un orden específico.
- Se utilizan para realizar operaciones de conjunto como unión, intersección y diferencia.

```python
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}

# Unión
print(my_set1 | my_set2)

# Intersección
print(my_set1 & my_set2)

# Diferencia
print(my_set1 - my_set2)
```