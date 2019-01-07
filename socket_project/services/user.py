from socket_project.dao.user_dao import get_user


def get_user_service(id):
    user = get_user(id)
    if user is None:
        user = ""
    return user


