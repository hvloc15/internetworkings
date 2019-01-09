import socket
import threading
from socket_project.exceptions import NotFoundError
from socket_project.url_lib.url_resolve import match_url
from socket_project.exceptions import MyException
from socket_project.json_response import JsonResponse
import json
from socket_project import urls
from socket_project import settings
import re
from base64 import b64encode
from hashlib import sha1
from socket_project.websocket import websocket_helper
from socket_project.cache import cache


class MySocket(websocket_helper.WebSocketHelper):

    def get_view(self, request):
        for url_pattern in urls.URL.keys():
            params =  match_url(request, url_pattern)
            if params is not None:
                return urls.URL[url_pattern], params
        raise NotFoundError("URL Not found")

    def handleMessage(self):
        request = json.loads(self.data)
        try:
            print(request["URL"])
            view_func, params = self.get_view(request)
            params['client'] = self
            message = view_func(request, **params)
        except MyException as e:
            message = JsonResponse(e.status_code, e.message).as_json(error_message=True)
        except Exception as e:
            message = JsonResponse(400, str(e)).as_json(error_message=True)

        self.sendMessage(message)

    def handleClose(self):
        cache.delete(self.username)

class Server:
    def __init__(self, host, port, number_of_connection):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(number_of_connection)
        self.client_connection = {}

    def _handleClose(self, client):
        client.client.close()
        if client.handshaked:
            try:
                client.handleClose()
            except:
                pass


    def handle_handshake(self, connection):
        text = connection.recv(1024).decode()
        key = (re.search('Sec-WebSocket-Key:\s+(.*?)[\n\r]+', text)
               .groups()[0]
               .strip())
        my_key = (key.encode('ascii') + settings.GUID.encode('ascii'))
        response_key = b64encode(sha1(my_key).digest()).decode('ascii')
        response = '\r\n'.join(settings.WEBSOCKET_ANSWER).format(key=response_key)
        connection.send(response.encode('ascii'))

    def accept_connection(self):
        print("start")
        while True:
            connection = None
            try:
                connection, address = self.server_socket.accept()
                print(connection)
                client = MySocket(connection, address)
                self.handle_handshake(connection)
                threading.Thread(target=self.handle_client, args=(client,)).start()
            except Exception as n:
                print("Connection Error: ",n)
                if connection is not None:
                    connection.close()

    def handle_client(self, client):
        while True:
            try:
                client.handshaked = True
                client._handleData()
                self.send_message(client)
            except Exception as n:
                self._handleClose(client)
                return


    def send_message(self, client):
        try:
            while client.sendq:
                opcode, payload = client.sendq.popleft()
                remaining = client._sendBuffer(payload)
                if remaining is not None:
                    client.sendq.appendleft((opcode, remaining))
                    break
                else:
                    if opcode == websocket_helper.CLOSE:
                        raise Exception('received client close')

        except Exception as n:
            self._handleClose(client)

    #
    # def handle_client(self, connection, address):
    #     data = connection.recv(2048).decode('utf-8')
    #     print(data)
    #
    #     #connection.recv(8192).decode(
    #
    #     request = json.loads(data)
    #     try:
    #         print(request["URL"])
    #         view_func, params = self.get_view(request)
    #         message = view_func(request, **params)
    #     except MyException as e:
    #         message = JsonResponse(e.status_code, e.message).as_json(error_message=True)
    #     except Exception as e:
    #         message = JsonResponse(400, str(e)).as_json(error_message=True)
    #
    #     connection.sendall(message.encode())
    #     self.remove_client_connection(address)

    def remove_client_connection(self, address):
        lock = threading.Lock()
        lock.acquire()
        del self.client_connection[address]
        lock.release()



server = Server(settings.HOST, settings.PORT, settings.NUMBER_OF_CONNECTION)
server.accept_connection()
