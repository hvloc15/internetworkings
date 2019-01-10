from socket_project.dao.chat_dao import get_list_message, send_message
from socket_project.cache import cache

def get_list_message_service(request, friend_id):
    page = request.get("page", "0")
    page_size = request.get("page_size", "20")
    return get_list_message(request["User"]["id"], friend_id, page, page_size)


def notify_typing_service(request, friend_username):
    notify_friend(friend_username, {"User": request["User"], "isTyping": 1})


def notify_friend(friend_username, message):
    connection = cache.get(friend_username)
    connection.sendMessage(message)


def send_message_service(request):
    body = request["DATA"]
    userid = request["User"]["id"]
    friend_id = body["id"]
    friend_username = body["username"]
    content = body["content"]
    date = body["date"]

    send_message(userid,friend_id,content,date)
    notify_friend(friend_username, {"User": request["User"], "content": content, "date":date})
