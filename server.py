import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host= socket.gethostname()
port=12345

server_socket.bind((host, port))


server_socket.listen(5)

print(f"server listening on {host}.{port}... ")
client_socket, addr=server_socket.accept()
print(f"got connection from {addr}")
while True:


    message=input()
    client_socket.send(message.encode('ascii'))
    message1=client_socket.recv(1024)
    print(f"messag from server:{message1.decode ('ascii')}")


client_socket.close()