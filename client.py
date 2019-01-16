#CLIENT

import socket, threading, json

class Client:
    def __init__(self):
        self._username = "User"

        self._serverHost = "127.0.0.1"

        self._port = 4500

        self._socket = None

        print("Pager Client\n")

        self.loadConfig()

        self.connect()

        self.runloop()

    def __del__(self):
        pass

    def runloop(self):
        getThread = threading.Thread(target = self.getMessages)
        sendThread = threading.Thread(target = self.sendMessage)

        getThread.start()
        sendThread.start()

    def connect(self):
        try:
            self._socket = socket.socket()

            self._socket.connect((self._serverHost, self._port))

            self._connected = True

            print("Connected to server!\n")
            
        except:
            pass

    def getMessages(self):
        while True:
            data = self._socket.recv(1024).decode()

            if data:
                print(data)

    def sendMessage(self):
        while True:
            data = input("")

            message = json.dumps({"data": data, "username": self._username})

            self._socket.send(message.encode())

    def loadConfig(self):
        try:
            with open("config.json") as file:
                configData = json.load(file)

            self._serverHost = configData["serverHost"]
            self._port = configData["port"]
            self._username = configData["username"]

        except:
            pass


try:
    client = Client()

except:
    print("Connection closed!")
    input()
