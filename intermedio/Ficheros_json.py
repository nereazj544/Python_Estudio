# .json file
import json

json_file_equipos = open("intermedio/doc/my_file_equiposIE.json", "w+")  # Crear un fichero JSON
json_file_jugadores = open("intermedio/doc/my_file_jugadoresIE.json", "w+")  # Crear un fichero JSON

json_data = {
    "Nombre": "Ragnah",
    "Liga": "Japon",
    "Entrenador": "-",
    "Capitan": "Simeon",
    "Jugadores": [ "Simeon"]
}


json_data2 = {
        "Nombre": "Simeon",
        "Posiciones": "DL",
        "Equipos": "Ragnah"
    }

json.dump(json_data, json_file_equipos)
json.dump(json_data2, json_file_jugadores)
