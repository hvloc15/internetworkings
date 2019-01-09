from socket_project.dao.friend_dao import get_list_friend_username, accept_friend, add_friend, \
    cancle_friend_request, get_list_requested_friend, get_list_stranger
from socket_project.exceptions import FriendshipError, BadRequest
from socket_project.dao.user_dao import get_user_by_username

def get_list_friend_service(request):
    id = request["User"]["id"]
    status = request.get("isrequested")
    if status is not None:
        if status == "1":
            return get_list_requested_friend(id=id)
        else:
            return get_list_stranger(id=id)
    else:
        return get_list_friend_username(id =id)


def check_duplicate_id(userid, friendid):
    if userid == friendid:
        raise FriendshipError


def accept_friend_service(userid, friend_username):
    accept_friend(userid, friend_username)
    user = get_user_by_username(friend_username)
    if user is None:
        raise BadRequest("Cannot find user with username: " + friend_username)
    return user

def add_friend_service(userid, friend_username):
    try:
        add_friend(userid, friend_username)
        user = get_user_by_username(friend_username)
        if user is None:
            raise BadRequest("Cannot find user with username: " + friend_username)
        return user
    except Exception:
        raise BadRequest("Friend is already added or requested")


def cancle_friend_request_service(userid, username):
    cancle_friend_request(userid, username)
