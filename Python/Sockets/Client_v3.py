import socket
HOST = "127.0.0.1"
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP

s.connect((HOST, PORT))

while "Exit":  
    # Bucle para enviar mensajes hasta que se envíe "Exit"
    msg = input("Escribe un mensaje (o 'e x i t' para salir): ")  # Solicita al usuario un mensaje
    s.sendall(msg.encode())  # Envía el mensaje al servidor
    if msg.lower() == "exit":  # Si el usuario escribe "Exit", se sale del bucle
        break
    s.sendall(msg.encode())  # Envía el mensaje al servidor

