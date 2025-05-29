## CLASES

class Persona:
    #esto es como un constructor en otros lenguajes
    # __init__ es un método especial que se llama al crear una instancia de la clase
    def __init__(self, nombre, surname, alias = "Sin alias"):
        # self.nombre = nombre
        # self.edad = edad

        self.full_name = f"{nombre} {surname} ({alias})"

    def saludar(self):
        print(f"Hola, {self.full_name}.")

    def sentado(self):
        print(f"{self.full_name} está sentado.")

# Crear una instancia de la clase Persona
name = input("Introduce el nombre de la persona: ")
surname = input("Introduce el apellido de la persona: ")
alias = input("Introduce el alias de la persona (opcional): ")
# age = int(input("Introduce la edad de la persona: "))


persona = Persona(name, surname, alias)
print(persona.full_name)  # Imprime el nombre completo de la persona
# Llamar al método saludar
persona.saludar()
persona.sentado()

my_other_persona = Persona("Juan", "Pérez", "Juampi")
print(my_other_persona.full_name)  # Imprime el nombre completo de la persona
# Llamar al método saludar
my_other_persona.saludar()
my_other_persona.sentado()
