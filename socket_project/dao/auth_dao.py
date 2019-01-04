import settings
from socket_project.utils.utils import annotate


def login(username, password):

    sql = """SELECT id, username
             FROM user
             WHERE username = %s and password = %s
            """
    #result = settings.db_instance.query(sql, (username, hashlib.md5(password).hexdigest()))
    result = settings.db_instance.query(sql, (username, password))
    return annotate( result, ("id", "username")) if result is not None else None
