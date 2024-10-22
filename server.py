import socket
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

quiz_data = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who is the author of 'Romeo and Juliet'?": "William Shakespeare",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What is the tallest mammal on Earth?": "Giraffe",
    "What is the chemical symbol for water?": "H2O",
}


def start_quiz(connection):
    for question, answer in quiz_data.items():
        connection.sendall(question.encode())
        client_response = connection.recv(1024).decode()
        if client_response.lower() == answer.lower():
            connection.sendall("Correct!\n".encode())
        else:
            connection.sendall(f"Incorrect. The correct answer is {answer}.\n".encode())

    connection.sendall("Quiz completed. Goodbye!\n".encode())

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server IP and port
    server_socket.bind((SERVER_IP, SERVER_PORT))

    # Listen for incoming connections
    server_socket.listen(2)
    print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Start the quiz for the connected client
        start_quiz(client_socket)

        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    main()
