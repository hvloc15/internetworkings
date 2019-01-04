import socket
import threading
from socket_project.exceptions import NotFoundError
from socket_project.url_lib.url_resolve import match_url
from socket_project.exceptions import MyException
from socket_project.json_response import JsonResponse
import json
from socket_project import urls
from socket_project import settings


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

    def get_view(self, url):
        for url_pattern in urls.URL.keys():
            if match_url(url, url_pattern) is not None:
                return urls.URL[url_pattern]

        raise NotFoundError

    def handle_client(self, connection, address):
        request = json.loads(connection.recv(8192).decode())
        try:
            view_func = self.get_view(request.get("URL"))
            message = view_func(request)
        except MyException as e:
            message = JsonResponse(e.status_code, e.message).as_json(error_message=True)
        except Exception as e:
            message = JsonResponse(400, str(e)).as_json(error_message=True)

        connection.sendall(message.encode())
        self.remove_client_connection(address)

    def remove_client_connection(self, address):
        lock = threading.Lock()
        lock.acquire()
        del self.client_connection[address]
        lock.release()

server = Server(settings.HOST, settings.PORT, settings.NUMBER_OF_CONNECTION)
server.accept_connection()

