import socket

def send_payload(payload):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    print("Connected to the server.")

    try:
        client_socket.send(payload.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Server: {response.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    payloads = [
        "Hello, Server!",
        "A" * 1024,  # Buffer overflow test
        "' OR '1'='1",  # SQL injection test
        "<script>alert('XSS')</script>",  # XSS test
        "DROP TABLE users;",  # SQL injection test
    ]

    for payload in payloads:
        print(f"Sending payload: {payload}")
        send_payload(payload)