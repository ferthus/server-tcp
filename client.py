"""
This module implement the client for use Socket TCP.
request to user the text that send the server.
with DESCONEXION command, the connection is finalized

use the next environment:
:param CLIENT_HOST: default value es `localhost`
:param CLIENT_PORT: default value es `5000`
"""

import socket
import os


SIZE_WORK = 1024
try:
    HOST = os.environ['CLIENT_HOST']
except KeyError:
    HOST = "localhost"

try:
    PORT = int(os.environ['CLIENT_PORT'])
except KeyError:
    PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        usr_text = input("prompt: ")
        client_socket.sendall(usr_text.encode('utf-8'))
        response = client_socket.recv(SIZE_WORK).decode('utf-8')
        print(f"server: {response}\n")

except socket.error as e:
    print(f"\n\n Error de conexión {e}")

except KeyboardInterrupt:
    print("\n\n Conexión finalizada por el usuario")

finally:
    client_socket.close()
