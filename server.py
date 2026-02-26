import socket
HOST = "127.0.0.1" 
PORT = 12345       
# TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT)) 
server_socket.listen()      
print(f"Server http://{HOST}:{PORT} da ishlayapti...")
while True:
    conn, addr = server_socket.accept() 
    print(f"Ulandi: {addr}")

    data = conn.recv(1024) 
    if not data:
        break
    print("Clientdan keldi:", data.decode())
    conn.sendall(data) 
    conn.close()
