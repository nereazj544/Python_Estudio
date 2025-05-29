## CLASES

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
name = input("Introduce el nombre de la persona: ")
age = int(input("Introduce la edad de la persona: "))

persona = Persona(name, age)
# Llamar al método saludar
persona.saludar()