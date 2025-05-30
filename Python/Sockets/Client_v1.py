import socket
import threading
import time


HEADER = 64 # Este es el tamaño del header que se usara para enviar los mensajes # This is the size of the header that will be used to send messages
FORMAT = 'utf-8' # Este es el formato de codificacion que se usara para enviar los mensajes # This is the encoding format that will be used to send messages
PORT = int(6000)
# IP = str("127.0.0.1")  
SERVER = "192.168.167.39"
DISCONNECT_MESSAGE = "[!DESCONECTADO]" # Este es el mensaje que se enviara al cliente cuando se desconecte # This is the message that will be sent to the client when it disconnects
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket TCP  # Created a TCP socket
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) # Codifica el mensaje en el formato especificado # Encodes the message in the specified format
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len)) # Rellena el header con espacios hasta que tenga el tamaño especificado # Fills the header with spaces until it reaches the specified size
    client.send(send_len)
    client.send(message)

send("Hola, soy el cliente") # Envía un mensaje al servidor # Sends a message to the server