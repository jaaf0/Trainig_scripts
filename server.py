import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Client: "+data)
            response = input("Server: ")
            conn.send(response.encode())
    except KeyboardInterrupt:
        print("Server stopped by user.")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()