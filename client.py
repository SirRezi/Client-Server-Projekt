import socket

# Serverkonfiguration
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Verbindung zum Server herstellen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((SERVER_IP, SERVER_PORT))
print('Verbindung zum Server hergestellt.')

while True:
    # Daten vom Benutzer eingeben
    message = input('Nachricht eingeben: ')
    if message.lower() == 'exit':
        break

    # Daten an den Server senden und Antwort empfangen
    server_socket.sendall(message.encode())
    data = server_socket.recv(1024)
    print('Antwort vom Server:', data.decode())

# Verbindung zum Server beenden
server_socket.close()
print('Verbindung beendet.')
