from socket_project.dao.auth_dao import login, signup, update_online_state, logout
from socket_project.dao.friend_dao import get_list_friend_username, get_list_friend_by_id
from socket_project.exceptions import AuthenticationFailed, SignupError
from socket_project.jwt_helper.jwt_helper import jwt_encode_handler, jwt_payload_handler
from socket_project.cache import cache
import json


def login_service(username, password, client):
    # if cache.get(username) is not None:
    #     raise AuthenticationFailed("Already login")

    if username == '' or password == '':
        raise AuthenticationFailed

    user = login(username, password)
    if user is None:
        raise AuthenticationFailed

    update_online_state(user["id"])
    user["isOnline"] = 1

    client.username = username
    client.id = user["id"]
    cache.set(username, client)

    json_response = {"data": {
        "id": user["id"],
        "username": user["username"]
    },
        "url": "online",
        "method": "GET",
        "status": 200
    }

    notify_friend(get_list_friend_username(id=user["id"]), json_response)

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return token, user


def notify_friend(list_friend, json_response):
    for friend in list_friend:
        client_conn = cache.get(friend["username"])
        if client_conn is None:
            continue

        client_conn.my_send_message(json.dumps(json_response))


def signup_service(username, password, date_of_birth):
    try:
        return signup(username,password, date_of_birth)
    except Exception as e:
        raise SignupError


def logout_service(id):
    logout(id)

    json_response = {"data": {
        "id": id
    },
        "url": "offline",
        "method": "GET",
        "status": 200
    }
    notify_friend(get_list_friend_username(id=id), json_response)

