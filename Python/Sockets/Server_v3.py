import socket

HOST = "127.0.0.1"
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP

server.bind((HOST, PORT))
server.listen(5)  # Escucha conexiones entrantes
while True:
    conn, addr = server.accept()  # Acepta una conexión entrante
    print(f"Conectado a {addr}")  # Imprime la dirección del cliente conectado
    print("Esperando datos del cliente...")
    msg = conn.recv(1024).decode()  # Recibe datos del cliente
    conn.close()  # Cierra la conexión
    print(f"[{addr}] {msg}")
