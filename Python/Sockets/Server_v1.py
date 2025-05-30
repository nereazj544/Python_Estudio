import socket
import threading
import time

HEADER = 64 # Este es el tamaño del header que se usara para enviar los mensajes # This is the size of the header that will be used to send messages
FORMAT = 'utf-8' # Este es el formato de codificacion que se usara para enviar los mensajes # This is the encoding format that will be used to send messages
PORT = int(6000)
# IP = str("127.0.0.1")  
SERVER = socket.gethostbyname(socket.gethostname()) # Obtiene la IP del servidor # Gets the server's IP
ADDR = (SERVER, PORT) # Crea una tupla con la IP y el puerto # Creates a tuple with the IP and port
DISCONNECT_MESSAGE = "[!DESCONECTADO]" # Este es el mensaje que se enviara al cliente cuando se desconecte # This is the message that will be sent to the client when it disconnects

print(f"Server name: {socket.gethostname()} - IP and Port: {SERVER}:{PORT} ") # Esto imprime el nombre del servidor y su IP # This prints the server name and its IP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket TCP  # Created a TCP socket
server.bind(ADDR) # Asocia el socket a la IP y el puerto

#Comunicacion con el cliente # Communication with the client
# Esta funcion se encarga de manejar la comunicacion con el cliente # This function handles communication with the client
def client_hilo (conn, addr):
    print("[NEW CONNECTION] {addr} conectado.") # Esto imprime que un nuevo cliente se ha conectado # This prints that a new client has connected
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT) # Recibe el mensaje del cliente y lo decodifica # Receives the message from the client and decodes it
        msg_len = int(msg_len) # Convierte el mensaje a un entero # Converts the message to an integer
        msg = conn.recv(msg_len).decode(FORMAT) # Recibe el mensaje del cliente y lo decodifica # Receives the message from the client and decodes it
        if msg == DISCONNECT_MESSAGE: # Si el mensaje es el de desconexion, se cierra la conexion # If the message is the disconnect message, the connection is closed
            connected = False # Cambia el estado de la conexion a desconectado # Changes the connection state to disconnected
        
        print(f"[{addr}] {msg}") # Esto imprime el mensaje del cliente # This prints the client's message

    conn.close() # Cierra la conexion con el cliente # Closes the connection with the client

def start():
    server.listen() # El servidor se pone a la escucha de conexiones entrantes # The server starts listening for incoming connections
    print(f"[LISTENING] Server esta escuchando en {SERVER}:{PORT}") # Esto imprime que el servidor está escuchando en la IP y el puerto # This prints that the server is listening on the IP and port
    while True:
        conn, addr = server.accept()
        print(f"[NEW CLIENT] {addr} conectado.")
        thread = threading.Thread(target=client_hilo, args=(conn, addr))
        thread.start() # Esto inicia un nuevo hilos para manejar al cliente # This starts a new thread to handle the client
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # Esto imprime el numero de conexiones activas # This prints the number of active connections






print("[STARTING] Server esta iniciado.. ") # Esto imprime que el servidor está iniciado # This prints that the server is starting
start()