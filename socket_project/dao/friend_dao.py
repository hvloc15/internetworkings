import settings
from socket_project.utils.utils import annotate


def get_list_friend(id, isonline = None, isrequested=None):
    sql = """SELECT user.id, user.username, user.dateofbirth, user.avatar
             FROM friendship join user on (friendship.friendid = user.id)
             WHERE friendship.userid = %s and friendship.status = %s
            """
    params = [id]
    params.append("active") if isrequested is None else params.append("inactive")

    if isonline is not None:
        sql += " user.isonline = %s"
        params.append(isonline)

    result = settings.db_instance.query(sql, params)
    return [annotate(record, ("id", "username", "date_of_birth", "avatar")) for record in result]


def accept_friend(userid, friendid):
    sql = """UPDATE friendship
             SET status='active'
             WHERE (userid = %s and friendid=%s) or (userid = %s and friendid=%s)
               """
    settings.db_instance.execute_sql(sql,(userid, friendid, friendid, userid))


def add_friend(userid, friendid):
    sql = """INSERT INTO friendship (userid, friendid, status)
             VALUES (%s,%s,%s)
               """
    settings.db_instance.execute_sql(sql, (userid, friendid,'inactive'))
    settings.db_instance.execute_sql(sql, (friendid, userid,'inactive'))


def cancle_friend_request(userid, friendid):
    sql = """DELETE FROM friendship
             WHERE ((userid=%s and friendid=%s) or (userid=%s and friendid=%s))and status = 'inactive'
               """
    settings.db_instance.execute_sql(sql, (userid, friendid, friendid, userid))
