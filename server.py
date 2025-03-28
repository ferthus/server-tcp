"""
This module implement the server for use Socket TCP.
accepts the connection of a one client and response the
text received in capital letters. with DESCONEXION command
received of the client then, the connection finalized

use the next environment:
:param SERVER_HOST: default value `localhost`
:param SERVER_PORT: default value `5000`
"""
import os
import socket


SIZE_WORK = 1024
try:
    HOST = os.environ['SERVER_HOST']
except KeyError:
    HOST = "localhost"

try:
    PORT = int(os.environ['SERVER_PORT'])
except KeyError:
    PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"\tConexión establecida desde {addr}")

    try:
        while True:
            data = conn.recv(SIZE_WORK)  # Recibir datos
            if not data:
                print("Se cierra la conexión con el cliente\n\n")
                break

            print(f"\tCliente dice: {data.decode('utf-8')}")
            cmd = data.decode('utf-8')
            response = cmd.upper()
            if cmd == "DESCONEXION":
                response = "bye"
                print(f"\t*** {cmd} *** \n\n")
                break

            conn.sendall(response.encode('utf-8'))

    except socket.error as msg:
        print(msg)
    finally:
        conn.close()
