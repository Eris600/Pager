#SERVER

import socket, threading, json

class Server:
    def __init__(self):
        self._ownHost = "127.0.0.1"

        self._ports = [ 4500, 4510, 4520, 4530, 4540, 4550 ]

        self._sockets = []
        self._connections = []
        
        print("Pager Server\n{}\n".format(self._ownHost))

        for port in self._ports:
            newThread = threading.Thread(target = self.connect, args = (port,))
            newThread.start()

        self.runloop()

    def __del__(self):
        for conn in self._connections:
            conn.close()

    def runloop(self):
        while True:
            self.getMessages()

    def connect(self, port):
        newSocket = socket.socket()

        newSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        newSocket.bind((self._ownHost, port))

        newSocket.listen(1)
        newConn, newAddr = newSocket.accept()

        self._sockets.append(newSocket)
        self._connections.append(newConn)

        self._connected = True

        print("Connected to {}, port {}!".format(newAddr[0], newAddr[1]))

    def getMessages(self):
        for conn in self._connections:
            message = conn.recv(1024).decode()

            if message:
                data = json.loads(message)

                text = "[{}]: {}".format(data["username"], data["data"])

                print(text)

                self.sendMessage(text)

    def sendMessage(self, message):
        for conn in self._connections:
            conn.send(message.encode())


server = Server()
