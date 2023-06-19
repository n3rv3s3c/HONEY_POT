import socket

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
        print(f"Incoming connection from: {address[0]}:{address[1]}")
        
        # Log the connection attempt
        with open("honeypot_log.txt", "a") as log_file:
            log_file.write(f"Incoming connection from: {address[0]}:{address[1]}\n")
        
        # Close the client connection
        client_socket.close()

if __name__ == '__main__':
    port = 8080  # Change this to the desired port number
    honeypot(port)
