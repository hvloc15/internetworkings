import socket
import threading

HOST = "127.0.0.1"
PORT = 65432
NUMBER_OF_CONNECTION = 5


class Server:

    def __init__(self, host, port, number_of_connection):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(number_of_connection)
        self.client_connection = {}

    def accept_connection(self):
        while True:
            connection, address = self.server_socket.accept()
            if self.client_connection.get(address) is None:
                self.client_connection[address] = connection
                threading.Thread(target=self.handle_client, args=(connection, address,)).start()

    def handle_client(self, connection, address):
        request = connection.recv(8192)
        view_func = self.get_view(request.get("URL"))
        message = view_func(request)
        connection.sendall(message)
        self.remove_client_connection(address)

    def get_view(self, url):
        pass

    def remove_client_connection(self, address):
        lock = threading.Lock()
        lock.acquire()
        del self.client_connection[address]
        lock.release()





server = Server(HOST, PORT, NUMBER_OF_CONNECTION)
server.accept_connection()