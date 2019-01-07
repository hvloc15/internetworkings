import settings
from socket_project.utils.utils import annotate


def get_user(id):
    sql = """SELECT id, username, dateofbirth, avatar
             FROM user
             WHERE id = %s
            """
    result = settings.db_instance.query(sql, (id,))[0]
    return annotate( result, ("id", "username", "date_of_birth", "image")) if result is not None else None

