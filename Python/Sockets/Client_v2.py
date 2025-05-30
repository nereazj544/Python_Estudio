import socket

HOST = '127.0.0.1'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Conecta al servidor
    print(f"Conectado al servidor en {HOST}:{PORT}")
    
    # la b indica que es un byte string
    s.sendall(b'Hola, soy el cliente')  # Envía un mensaje al servidor

    data = s.recv(1024)  # Recibe la respuesta del servidor
    print(f"Recibido del servidor: {data.decode('utf-8')}")  # Imprime los datos recibidos del servidor