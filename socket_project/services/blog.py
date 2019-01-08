from socket_project.dao.blog_dao import create_blog
from socket_project.exceptions import UnprocessableError


def create_blog_service(userid, content, date):
    try:
        create_blog(userid, content, date)
    except Exception:
        raise UnprocessableError
