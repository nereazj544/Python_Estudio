# Modules

#importar modulos de clases
import Clases
# Importar la clase Persona desde el módulo Clases
from Clases import Persona


#no es como java o c# que tienes que hacer: persona p = new Persona(); se crea directamente la instancia
# Crear una instancia de la clase Persona
p = Persona("Carlos", "Gómez", "Carlitos")  
p.saludar()  # Llamar al método saludar de la instancia p


