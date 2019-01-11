import settings
from socket_project.utils.utils import annotate
from socket_project.dao.user_dao import get_user_id


def get_list_friend(id, isonline = None, isrequested=None):
    sql = """SELECT user.id, user.username, user.dateofbirth, user.avatar
             FROM friendship join user on (friendship.friendid = user.id)
             WHERE friendship.userid = %s and friendship.status = %s
            """
    params = [id]
    params.append("active") if isrequested is None and isrequested==0 else params.append("inactive")

    if isonline is not None:
        sql += " user.isonline = %s"
        params.append(isonline)

    result = settings.db_instance.query(sql, params)
    if result is None:
        return []
    return [annotate(record, ("id", "username", "date_of_birth", "avatar")) for record in result]

def get_list_requested_friend(id):
    sql = """SELECT user.id, user.username, user.dateofbirth, user.avatar, user.isonline, friendship.status
             FROM friendship join user on (friendship.friendid = user.id)
             WHERE friendship.userid = %s and (friendship.status = 'request' or friendship.status = 'accept')
            """
    params = (id,)
    query_result = settings.db_instance.query(sql, params)
    inactive_user = []
    if query_result is not None:
        inactive_user = [annotate(record, ("id","username","date_of_birth","avatar", "isOnline", "status")) for record in query_result]
    print("Inactive: "+ str(inactive_user))
    return inactive_user


def get_list_stranger(id):
    sql = """SELECT id, username, dateofbirth, avatar, isonline FROM user 
             WHERE user.id != %s AND NOT EXISTS(SELECT * FROM friendship WHERE userid= %s AND friendid= user.id)
            """
    params = (id,id)
    query_result = settings.db_instance.query(sql, params)
    if query_result is None:
        return []
    result = [annotate(record, ("id","username","date_of_birth","avatar", "isOnline")) for record in query_result]
    print("Strange: " +str(result))
    return result

def get_list_friend_username(id=None, username=None):
    if id is None:
        id = get_user_id(username)
        if id is None:
            return []

    sql = """SELECT user.id, user.username, user.dateofbirth, user.avatar, user.isonline
             FROM friendship join user on (friendship.friendid = user.id)
             WHERE friendship.userid = %s and friendship.status = 'active'
            """
    result = []
    records = settings.db_instance.query(sql, (id,))

    if records is None:
        return result

    result = [annotate(record, ("id","username","date_of_birth", "avatar","isOnline")) for record in records]
    print("Friend: "+ str(result))
    return result

def get_list_friend_by_id(id):
    sql = """SELECT user.id
                FROM friendship join user on (friendship.friendid = user.id)
                WHERE friendship.userid = %s and friendship.status = 'active'
               """

    records = settings.db_instance.query(sql, (id,))
    if records is None:
        return []
    return [record[0] for record in records]

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
    queries = [sql,sql]
    params = [(userid, friendid,'request'), (friendid, userid,'accept')]
    settings.db_instance.transaction(queries, params)


def cancle_friend_request(userid, friendid):

    sql = """DELETE FROM friendship
             WHERE ((userid=%s and friendid=%s) or (userid=%s and friendid=%s))and status = 'inactive'
               """
    settings.db_instance.execute_sql(sql, (userid, friendid, friendid, userid))

#add_friend(userid=1, friendid=5)
#cancle_friend_request(userid=1, friendid=5)
#print(get_list_friend_username("vinhloc"))
#print(get_list_friend_by_id(2))