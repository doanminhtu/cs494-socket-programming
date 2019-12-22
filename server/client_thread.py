import threading

class ClientThread(threading.Thread):
    """ Init and run thread for new connection  """

    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.client_address = clientAddress
        print("New connection added: ", clientAddress)

    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(8196)
            if data == b'':
                continue
            msg = data.decode()
            if msg == 'bye':
                break
            print("from client", msg)
            from utils import make_msg
            self.csocket.send(make_msg("hello", msg))
            self.csocket.send(make_msg("hello", msg))
        print("Client at ", self.client_address, " disconnected...")