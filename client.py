import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("localhost", 5000))

while True:
    # Read message from user
    message = input("Enter message: ")

    # Send message to server
    client.send(message.encode())

    if message.lower() == "exit":
        break

    # Receive echoed message
    data = client.recv(1024).decode()
    print("Echo from Server:", data)

# Close socket
client.close()