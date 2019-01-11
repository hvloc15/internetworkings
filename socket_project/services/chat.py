from socket_project.dao.chat_dao import get_list_message, send_message
from socket_project.dao.user_dao import get_user
from socket_project.cache import cache
from socket_project.exceptions import BadRequest
import json


def get_list_message_service(request, friend_id):
    page = request.get("page", "0")
    page_size = request.get("page_size", "20")
    return get_list_message(request["User"]["id"], friend_id, page, page_size)


def notify_typing_service(request, friend_username, type):

    json_response = {"data": {
        **request["User"],
        "type": type,
    },
        "url": "chat/istyping",
        "method": "POST",
        "status": 200
    }
    notify_friend(friend_username, json_response)


def notify_friend(friend_username, message):
    connection = cache.get(friend_username)
    if connection is None:
        return
    connection.my_send_message(json.dumps(message))


def send_message_service(request):
    body = request["DATA"]
    userid = request["User"]["id"]
    friend_id = body["id"]
    friend_username = body["username"]
    content = body["content"]
    date = body["date"]
    if userid == friend_id:
        raise BadRequest("Userid and friendid is the same")

    send_message(userid, friend_id, content, date)
    json_response = {"data": {
        **get_user(userid), "content": content, "date": date,
    },
        "url": "chat/receive",
        "method": "POST",
        "status": 200
    }
    notify_friend(friend_username, json_response)
