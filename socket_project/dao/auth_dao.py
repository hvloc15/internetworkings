import settings
from socket_project.utils.utils import annotate


def login(username, password):

    sql = """SELECT id, username, dateofbirth, avatar
             FROM user
             WHERE username = %s and password = %s
            """
    #result = settings.db_instance.query(sql, (username, hashlib.md5(password).hexdigest()))
    result = settings.db_instance.query(sql, (username, password))
    return annotate( result[0], ("id", "username","date_of_birth","avatar")) if result is not None else None


def update_online_state(id):
    sql = """UPDATE user
             SET isonline=1
             WHERE id = %s
               """
    settings.db_instance.execute_sql(sql,(id,))


def signup(username, password, date_of_birth):

    sql = """INSERT INTO user (username, password, dateofbirth)
             VALUES (%s,%s,%s)
            """
    settings.db_instance.execute_sql(sql, (username, password, date_of_birth))
    return True


def logout(username):

    sql = """UPDATE user SET isonline=0 WHERE username=%s"""
    #result = settings.db_instance.query(sql, (username, hashlib.md5(password).hexdigest()))
    result = settings.db_instance.query(sql, (username,))

