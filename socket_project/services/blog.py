from socket_project.dao.blog_dao import create_blog, get_list_blog
from socket_project.dao.friend_dao import get_list_friend_username, get_list_friend_by_id
from socket_project.exceptions import UnprocessableError
from socket_project.cache import cache
import json


def create_blog_service(request):
    body = request["DATA"]
    userid = request["User"]["id"]
    content = body["content"]
    date = body["date"]
    try:
        create_blog(userid, content, date)

        json_response = {"data": {
            "id": userid,
            "content": body["content"],
            "date": body["date"]
        },
            "url": "newblog",
            "method": "GET",
            "status": 200
        }
        list_friend =  get_list_friend_username(id=userid)
        list_friend.append({"username": request["User"]["username"]})
        notify_friend(list_friend, json_response)
    except Exception:
        raise UnprocessableError


def notify_friend(list_friend, json_response):
    for friend in list_friend:
        client_conn = cache.get(friend["username"])
        if client_conn is None:
            continue

        client_conn.my_send_message(json.dumps(json_response))


def get_list_blog_service(request):
    id = request["User"]["id"]
    page = request.get("page", "0")
    page_size = request.get("page_size", "5")

    friend_ids = get_list_friend_by_id(id=id)
    friend_ids.append(id)

    return get_list_blog(friend_ids,page,page_size)







