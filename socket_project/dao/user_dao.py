import settings
from socket_project.utils.utils import annotate


def get_user(id):
    sql = """SELECT id, username, dateofbirth, avatar
             FROM user
             WHERE id = %s
            """
    result = settings.db_instance.query(sql, (id,))
    return annotate( result[0], ("id", "username", "date_of_birth", "avatar")) if result is not None else None

def get_user_id(username):
    sql = """SELECT id
             FROM user
             WHERE username = %s
            """
    result = settings.db_instance.query(sql, (username,))
    return result[0][0] if result is not None else None


def get_user_by_username(username):
    sql = """SELECT id, username, dateofbirth, avatar, isonline
             FROM user
             WHERE username = %s
            """
    result = settings.db_instance.query(sql, (username,))
    return annotate(result[0], ("id", "username", "date_of_birth", "avatar", "isOnline")) if result is not None else None

