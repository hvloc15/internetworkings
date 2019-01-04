#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import threading
import json
HOST = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def handle_input(client_socket):
    input_string = {
        "METHOD": "POST",
        "URL": "users/login",
        "DATA":{
            "username":"vinhloc",
            "password":"1011988"
        }
    }
    client_socket.sendall(json.dumps(input_string).encode())


def handle_output(client_socket):
    string = client_socket.recv(1024)
    print("Receive: ", string.decode())


input_thread = threading.Thread(target=handle_input, args=(client_socket,))
output_thread = threading.Thread(target=handle_output, args=(client_socket,))

input_thread.start()
output_thread.start()
