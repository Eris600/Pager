#SERVER

import sender, reciever, threading, json

class Server:
    def __init__(self):
        self._ownHost = "127.0.0.1"
        self._addresses = [ ("127.0.0.1", 4500),
                           ("127.0.0.1", 4510),
                           ("127.0.0.1", 4520),
                           ("127.0.0.1", 4530),
                           ("127.0.0.1", 4540) ]

        #self._port = 5000

        self._senders = []
        self._recievers = []

        for address in self._addresses:
            newThread = threading.Thread(target = self.connect, args = (address,))
            newThread.start()
            
            #asyncio.run(self.connect(host))

        self.runloop()

    def __del__(self):
        for sender in self._senders:
            del sender

        for reciever in self._recievers:
            del reciever

    def runloop(self):
        while True:
            self.getMessages()

    def connect(self, address):
        newReciever = reciever.Reciever()
        newSender = sender.Sender()

        newReciever.connect(address[0], address[1])

        print("Connected reciever for {}...".format(address[0]))

        #while True:
        #    if newReciever.getMessages() == "READY":
        #        print("Ready recieved!")
        #        break

        newSender.connect(self._ownHost, address[1] + 1)

        print("Connected sender for {}...".format(address[0]))

        self._recievers.append(newReciever)
        self._senders.append(newSender)

        print("Fully connected to {}!".format(address[0]))

    def getMessages(self):
        for reciever in self._recievers:
            message = reciever.getMessages()
            
            if message:
                data = json.loads(message)

                text = "[{}]: {}".format(data["username"], data["data"])

                print(text)

                self.sendMessage(text)

    def sendMessage(self, message):
        for sender in self._senders:
            sender.send(message)


server = Server()
