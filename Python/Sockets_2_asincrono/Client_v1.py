import socket

HOST = "127.0.0.1"
PORT = 6000

import Log 
from Log import client_log, client_error, client_warning, client_debug, client_critical

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP
s.connect((HOST, PORT))
client_log(f"Conectado al servidor en {HOST}:{PORT}")  # Registra la conexión al servidor

while "Exit":
    msg = input("Escribe un mensaje (o 'e x i t' para salir): ")  # Solicita al usuario un mensaje
    if msg.lower() == "exit":  # Si el usuario escribe "Exit", se sale del bucle
        client_log("Cliente ha salido del bucle de mensajes")
        break
    s.sendall(msg.encode())  # Envía el mensaje al servidor


    s.close()  # Cierra el socket
