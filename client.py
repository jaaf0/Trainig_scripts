import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    try:
        while True:
            msg = input("Client: ")
            client_socket.send(msg.encode('utf-8'))
            response = client_socket.recv(1024)
            if not response:
                break
            print(f"Server: {response.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Client stopped by user.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()