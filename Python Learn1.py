import socket

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))  # Change IP and port as needed
server_socket.listen(5)

print("Server listening...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")

    filename = 'Save.txt'  # Replace with the file you want to send
    with open(filename, 'rb') as file:
        file_data = file.read()

    client_socket.sendall(file_data)
    client_socket.close()
