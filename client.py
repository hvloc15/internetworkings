#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import threading

HOST = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def handle_input(client_socket):
    while True:
        input_string = input()
        client_socket.sendall(input_string.encode())


def handle_output(client_socket):
    while True:
        string = client_socket.recv(1024)
        print("Receive: ", string)


input_thread = threading.Thread(target=handle_input, args=(client_socket,))
output_thread = threading.Thread(target=handle_output, args=(client_socket,))

input_thread.start()
output_thread.start()
