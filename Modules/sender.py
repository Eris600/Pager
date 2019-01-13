#SENDER

import socket

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
