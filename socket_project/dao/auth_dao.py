import settings
from socket_project.utils.utils import annotate

def login(username, password):

    sql = """SELECT id, username
             FROM user
             WHERE username = %s and password = %s
            """
    #result = settings.db_instance.query(sql, (username, hashlib.md5(password).hexdigest()))
    result = settings.db_instance.query(sql, (username, password))[0]
    return annotate( result, ("id", "username")) if result is not None else None

def signup(username, password, date_of_birth):

    sql = """INSERT INTO user (username, password, dateofbirth)
             VALUES (%s,%s,%s)
            """
    settings.db_instance.execute_sql(sql, (username, password, date_of_birth))
    return True
