import socket

# Define the server IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to the quiz server.")

    # Receive and answer quiz questions
    while True:
        question = client_socket.recv(1024).decode()
        if not question:
            break  # No more questions, end the loop

        print("Question:", question)
        answer = input("Your answer: ")
        client_socket.sendall(answer.encode())

        # Receive and display server response
        response = client_socket.recv(1024).decode()
        print("Server:", response)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
