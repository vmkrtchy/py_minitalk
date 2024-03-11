import socket

while 1:

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",20012))

    msg = input("Client: ")
    s.send(str(msg).encode())

    reply = s.recv(1024).decode("utf-8")
    print("Server: " + reply)