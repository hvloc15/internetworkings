from socket_project.dao.auth_dao import login, signup
from socket_project.exceptions import AuthenticationFailed, SignupError
from socket_project.jwt_helper.jwt_helper import jwt_encode_handler, jwt_payload_handler


def login_service(username, password):
    user = login(username, password)
    if user is None:
        raise AuthenticationFailed

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token

def signup_service(username, password, date_of_birth):
    try:
        return signup(username,password, date_of_birth)
    except Exception as e:
        raise SignupError
