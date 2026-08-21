import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP address and port
server.bind(("localhost", 5000))

# Listen for client connection
server.listen(1)
print("Server is waiting for connection...")

# Accept client connection
conn, addr = server.accept()
print("Connected by:", addr)

while True:
    # Receive message from client
    data = conn.recv(1024).decode()

    if not data or data.lower() == "exit":
        print("Connection closed.")
        break

    print("Client:", data)

    # Echo the same message back to client
    conn.send(data.encode())

# Close connection
conn.close()
server.close()