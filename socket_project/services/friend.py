from socket_project.dao.friend_dao import get_list_friend_username, accept_friend, add_friend, \
    cancle_friend_request, get_list_requested_friend, get_list_stranger
from socket_project.exceptions import FriendshipError, BadRequest
from socket_project.dao.user_dao import get_user


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


def accept_friend_service(user_id, friend_id):
    check_duplicate_id(user_id, friend_id)
    accept_friend(user_id, friend_id)
    user = get_user(friend_id)
    if user is None:
        raise BadRequest("Cannot find user with username: " + friend_id)
    return user


def add_friend_service(request, friend_id):
    user_id = request["User"]["id"]
    check_duplicate_id(user_id, friend_id)
    try:
        add_friend(user_id, friend_id)
        user = get_user(friend_id)
        if user is None:
            raise BadRequest("Cannot find user with username: " + friend_id)
        user["requester"] = request["User"]["username"]
        return user
    except Exception:
        raise BadRequest("Friend is already added or requested")


def cancle_friend_request_service(user_id, friend_id):
    cancle_friend_request(user_id, friend_id)
