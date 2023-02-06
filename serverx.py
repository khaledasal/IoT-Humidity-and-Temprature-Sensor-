import socket
import threading
import paho.mqtt.client as paho
import os
import json
import time
from datetime import datetime

TOKEN1= 'swkHNZhMOct4pZa7Xx7R'  # Token of your device
TOKEN2 = 'i3GGBKOEYUtVgAZQSgsO'
broker = "demo.thingsboard.io"  # host name
port2 = 1883 # data listening port

def on_publish(client, userdata, result):  # create function for callback
    print("data published to thingsboard \n")
    pass

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

#IP='127.0.0.1'
port = 7000
ClientNumber = 0
ClientArray = []


ServerSocket.bind(("192.168.1.8", port))
print("socket binded to %s" % (port))


ServerSocket.listen(5)
print("socket is listening")


def threaded_client(Client, address):
    global ClientNumber
    global ClientArray
    client1 = paho.Client("control1")  # create client object
    if (ClientNumber == 1):
        client1.username_pw_set(TOKEN1)  # access token from thingsboard device
    else:
        client1.username_pw_set(TOKEN2)  # access token from thingsboard device
    client1.on_publish = on_publish  # assign function to callback
    client1.connect(broker, port2, )  # establish connection
    while True:
        x = Client.recv(1024).decode()
        y = Client.recv(1024).decode()
        payload = "{"
        payload += "\"Humidity\":" + x + ",";
        payload += "\"Temperature\":" + y;
        payload += "}"
        ret = client1.publish("v1/devices/me/telemetry", payload)  # topic-v1/devices/me/telemetry
        print("NEW DATA ENTERIES")
        print(payload);
        time.sleep(5)
    Client.close()

while True:

    client, address = ServerSocket.accept()
    ClientNumber += 1
    print('Got connection from', address)
    print('current number of clients', ClientNumber)
    ClientArray.append(address)
    print(' clients data ', ClientArray)

    Thread=threading.Thread(target=threaded_client, args=(client, address))
    Thread.start()