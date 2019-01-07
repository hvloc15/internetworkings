from socket_project.dao.friend_dao import get_list_friend, accept_friend, add_friend, cancle_friend_request
from socket_project.exceptions import FriendshipError, BadRequest


def get_list_friend_service(id):
    return get_list_friend(id)


def check_duplicate_id(userid, friendid):
    if userid == friendid:
        raise FriendshipError


def accept_friend_service(userid, friendid):
    check_duplicate_id(userid, friendid)
    accept_friend(userid, friendid)


def add_friend_service(userid, friendid):
    check_duplicate_id(userid, friendid)
    try:
        add_friend(userid, friendid)
    except Exception:
        raise BadRequest("Friend is already added or requested")

def cancle_friend_request_service(userid, friendid):
    cancle_friend_request(userid, friendid)
