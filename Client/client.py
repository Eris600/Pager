#CLIENT

import threading, json

class Reciever:
    def __init__(self):
        self._socket = None
        self._conn = None

        self._connected = False

    def __del__(self):
        pass

    def connect(self, host, port):
        self._socket = socket.socket()

        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self._socket.bind((host, port))

        self._socket.listen(1)
        self._conn, self._addr = self._socket.accept()

        self._connected = True

    def getMessages(self):
        data = self._conn.recv(1024).decode()

        return data if data else None

class Sender:
    def __init__(self):
        self._socket = None

        self._connected = False

    def __del__(self):
        try:
            self._socket.close()

        except:
            pass

    def connect(self, host, port):
        try:
            self._socket = socket.socket()
            self._socket.connect((host, port))

            self._connected = True

        except:
            pass

    def send(self, message):
        self._socket.send(message.encode())

class Client:
    def __init__(self):
        self._username = "User"

        self._ownHost = "127.0.0.1"
        self._serverHost = "127.0.0.1"

        self._port = 4500

        self._sender = None
        self._reciever = None

        self.loadConfig()

        self.connect()

        self.runloop()

    def __del__(self):
        del self._sender
        del self._reciever

    def runloop(self):
        #self.sendMessage()

        getThread = threading.Thread(target = self.getMessages)
        sendThread = threading.Thread(target = self.sendMessage)

        getThread.start()
        sendThread.start()

    def connect(self):
        self._sender = sender.Sender()
        self._reciever = reciever.Reciever()

        self._sender.connect(self._ownHost, self._port)

        self._reciever.connect(self._serverHost, self._port + 1)

        #self._sender.send("READY")

        print("Connected to server!\n")

    def getMessages(self):
        while True:
            message = self._reciever.getMessages()

            if message:
                print(message)

    def sendMessage(self):
        while True:
            data = input("")

            message = json.dumps({"data": data, "username": self._username})

            #print(message)

            self._sender.send(message)

    def loadConfig(self):
        try:
            with open("config.json") as file:
                configData = json.load(file)

            self._ownHost = configData["ownHost"]
            self._serverHost = configData["serverHost"]
            self._port = configData["port"]
            self._username = configData["username"]

        except:
            pass


client = Client()
