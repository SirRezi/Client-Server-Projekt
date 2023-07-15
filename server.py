# -*- coding: utf-8 -*-


import socket
import select

# Serverkonfiguration
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Erstelle einen Socket und binde ihn an die Server-IP und den Port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

# Warte auf eingehende Verbindungen
print('Server gestartet. Warte auf Verbindungen...')

while True:
    # Akzeptiere eingehende Verbindungen
    client_socket, client_address = server_socket.accept()
    print('Verbindung von:', client_address)

    # Empfange Daten vom Client und sende sie zurück
    while True:
        readable, _, _ = select.select([client_socket], [], [])
        if readable:
            data = client_socket.recv(1024)
            if not data:
                break
            print('Empfangene Daten:', data.decode())
            client_socket.sendall(data)

    # Beende die Verbindung zum Client
    client_socket.close()
    print('Verbindung beendet.')
