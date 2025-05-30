import socket

HOST = '127.0.0.1'
PORT = 6000

# Crea un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Asocia el socket a la dirección y puerto
    s.listen()  # Escucha conexiones entrantes
    con, addr = s.accept()  # Acepta una conexión entrante
    print(f"Servidor escuchando en {HOST}:{PORT}")

    with con:
        print(f"Conectado por {addr}")
        while True:
            data = con.recv(1024) # se queda esperando a recibir datos del cliente
            if not data:
                break
            con.sendall(data)

            

        data = con.recv(1024)
        
        

print(f"Recibido: {data}")  # Imprime los datos recibidos del cliente



