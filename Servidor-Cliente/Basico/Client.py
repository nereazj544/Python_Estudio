#! Importar librerias
import socket

#! Configuracion del cliente
HOST = "127.0.0.1" # Direccion IP del servidor
PORT = 6000 # Puerto del servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket TCP/IP
s.connect((HOST, PORT)) # Conecta al servidor



