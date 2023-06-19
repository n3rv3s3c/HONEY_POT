import socket
import threading
from datetime import datetime

def handle_client(client_socket, address):
    # Log the connection attempt with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] Incoming connection from: {address[0]}:{address[1]}"
    print(log_message)
    with open("honeypot_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")
    
    # Send a fake response to the client
    response = "Welcome to the honeypot!\n"
    client_socket.send(response.encode())
    
    # Close the client connection
    client_socket.close()

def honeypot(port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port
    server_socket.bind(('0.0.0.0', port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Honeypot listening on port {port}...")

    while True:
        # Accept a client connection
        client_socket, address = server_socket.accept()

        # Start a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == '__main__':
    port = 8080  # Change this to the desired port number
    honeypot(port)
