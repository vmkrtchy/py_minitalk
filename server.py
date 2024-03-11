import socket
from threading import Thread

def handleConnection(s, i):
    reply = s.recv(1024).decode("utf-8")
    print("Client: --->" + reply)

    message = input("Server: --->")
    s.send(str(message).encode("utf-8"))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",20012))
s.listen(5)
i = 0

while True:
    i += 1
    cs,addr = s.accept()
    t = Thread(target = handleConnection, args = (cs, i))
    t.start()