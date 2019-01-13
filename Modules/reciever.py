#RECIEVER

import socket

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
