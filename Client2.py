import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
port = 6790
s.connect(("172.20.10.3", port))
while True:
    message = input()
    s.send(message.encode())
    if message == "close":
        s.close()
        break
    print(s.recv(1024).decode())