#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import threading
import json
HOST = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


# def handle_input(client_socket):
#     input_string = {
#         "METHOD": "POST",
#         "URL": "users/login",
#         "DATA":{
#             "username":"vinhloc",
#             "password":"123456789"
#         }
#     }
#     client_socket.sendall(json.dumps(input_string).encode())
# def handle_input(client_socket):
#     input_string = {
#         "Method": "POST",
#         "URL": "users/signup",
#         "DATA":{
#             "username":"admin13",
#             "password":"admin",
#             "dateofbirth": 12312431
#         }
#     }
#     client_socket.sendall(json.dumps(input_string).encode())

def login(username, password):
    return {
        "Method": "POST",
        "URL": "users/login",
        "DATA":{
            "username":username,
            "password":password
        }
    }

def get_user():
    return {
        "Method": "GET",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ2aW5obG9jIiwiZXhwIjoxNTQ2OTUwOTMzfQ.p9tgcAHt5F8Mm_16lLLf8hQArKyZ2U9f2cei10OkrQw",
        "URL": "users/1",
    }

def get_friend(token):
    return {
        "Method": "GET",
        "Authorization": token,
        "URL": "friend?isonline=0",
    }

def add_friend():
    return {
        "Method": "POST",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ2aW5obG9jIiwiZXhwIjoxNTQ2OTUwOTMzfQ.p9tgcAHt5F8Mm_16lLLf8hQArKyZ2U9f2cei10OkrQw",
        "URL": "friend/add",
        "DATA": {
            "id": "2",
        }
    }

def accept_friend():
    return {
        "Method": "POST",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ2aW5obG9jMSIsImV4cCI6MTU0Njk2MDAzMn0.QzM92oLzeWFes8Xdx5z4PrM8iyoi2y59DGEdatnPmBI",
        "URL": "friend/accept",
        "DATA": {
            "id": "1",
        }
    }
def cancle_friend():
    return {
        "Method": "POST",
        "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ2aW5obG9jIiwiZXhwIjoxNTQ2OTUwOTMzfQ.p9tgcAHt5F8Mm_16lLLf8hQArKyZ2U9f2cei10OkrQw",
        "URL": "friend/cancle",
        "DATA": {
            "id": "2",
        }
    }

def add_blog():
    return {
        "Method": "POST",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ2aW5obG9jIiwiZXhwIjoxNTQ2OTUwOTMzfQ.p9tgcAHt5F8Mm_16lLLf8hQArKyZ2U9f2cei10OkrQw",
        "URL": "blog/create",
        "DATA": {
            "content": "Tinh nhu giac mong tan 4",
            "date": 1234567890
        }
    }
id1_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ2aW5obG9jIiwiZXhwIjoxNTQ3MDA4NDg1fQ._4AmjmDOWw3mw7oeoxfbzDfcJ61LZ1YtymBNmzq-K6U"
id2_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ2aW5obG9jMSIsImV4cCI6MTU0NzAwODQyNn0.bFRCNzeeNdbPo_yX35OwAeJGdjXvzZIvV5IALOcHiJ0"

def handle_input(client_socket):
    input = login("vinhloc2","123456789")
    #input = add_friend()
    #input = accept_friend()
    #input = add_blog()
    #input= get_friend(id1_token)
    client_socket.sendall(json.dumps(input).encode())


def handle_output(client_socket):
    string = client_socket.recv(1024)
    print("Receive: ", string.decode())


input_thread = threading.Thread(target=handle_input, args=(client_socket,))
output_thread = threading.Thread(target=handle_output, args=(client_socket,))

input_thread.start()
output_thread.start()
