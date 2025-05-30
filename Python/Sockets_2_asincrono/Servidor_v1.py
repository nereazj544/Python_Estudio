## SERVIDOR ASINCRONO 

# Librerias

import asyncio
import socket

from Log import server_log, server_error, server_warning, server_debug, server_critical

HOST = "127.0.0.1"
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP
server.bind((HOST, PORT))
server.listen(5)  # Escucha conexiones entrantes

async def task_client():
    server_log(f"Start server v1 connectes to {HOST}:{PORT}")
    try:
        while True:
            conn, addr = server.accept()
            server_log(f"Connected to {addr}")
            server_log("Waiting for data from client...")
            print("> Esperando datos del cliente...")

            while True:
                msg = conn.recv(1024).decode()
                if not msg:
                    conn.close()
                    print(f"> Conexión cerrada por {addr}")
                    server_log(f"Connection closed by {addr}")
                    break

                print(f"[{addr}] {msg}")
                server_log(f"[{addr}]")
                msg = input("Escribe una respuesta: ")
                conn.sendall(msg.encode())
    except socket.error as e:
        server_error(f"Error in task_client: {e}")
        print(f"> Error en la tarea del cliente: {e}")

