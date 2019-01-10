from socket_project.dao.auth_dao import login, signup, update_online_state, logout
from socket_project.dao.friend_dao import get_list_friend_username
from socket_project.exceptions import AuthenticationFailed, SignupError
from socket_project.jwt_helper.jwt_helper import jwt_encode_handler, jwt_payload_handler
from socket_project.cache import cache


def login_service(username, password, client):
    if cache.get(username) is not None:
        raise AuthenticationFailed("Already login")

    if username == '' or password == '':
        raise AuthenticationFailed

    user = login(username, password)
    if user is None:
        raise AuthenticationFailed

    update_online_state(user["id"])
    user["isOnline"] = 1

    cache.set(username, client)
    client.username = username
    notify_friend(get_list_friend_username(id=user["id"]))

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return token, user

def notify_friend(list_friend):
    for friend in list_friend:
        client_conn = cache.get(friend["username"])
        if client_conn is None:
            continue
        client_conn.sendMessage(friend["username"])

def signup_service(username, password, date_of_birth):
    try:
        return signup(username,password, date_of_birth)
    except Exception as e:
        raise SignupError

def logout_service(username):
    logout(username)
