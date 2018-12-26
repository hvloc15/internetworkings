import socket
import threading
from url_lib.url_resolve import get_view
from exceptions import MyException
from json_response import JsonResponse
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
        try:
            view_func = get_view(request.get("URL"))
            message = view_func(request)
        except MyException as e:
            message = JsonResponse(e.status_code, e.message).as_json()
        except Exception as e:
            message = JsonResponse(400, str(e)).as_json()

        connection.sendall(message)
        self.remove_client_connection(address)

    def remove_client_connection(self, address):
        lock = threading.Lock()
        lock.acquire()
        del self.client_connection[address]
        lock.release()





server = Server(HOST, PORT, NUMBER_OF_CONNECTION)
server.accept_connection()