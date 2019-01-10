import settings
from socket_project.utils.utils import annotate


def count_number_of_message(id):
    sql = """SELECT COUNT(*) from message WHERE senderid = %s or receiverid = %s
    """
    result = settings.db_instance.query(sql, (id, id))
    return result[0][0]


def get_list_message(id, friend_id, page, page_size=20):

    offset = page * page_size
    limit = page_size

    sql = """SELECT senderid, receiverid, content, date from message 
             WHERE (senderid =%s and receiverid= %s) or (senderid =%s and receiverid = %s)
             ORDER BY date DESC
             LIMIT %s,%s"""

    records = settings.db_instance.query(sql, (id,friend_id,friend_id, id, offset, limit))
    if records is None:
        return []

    result = [annotate(record, ("senderid", "receiverid", "content", "date")) for record in records]
    return result


def send_message(userid,friend_id,content,date):
    sql = """INSERT INTO message (senderid, receiverid, content, date)
             VALUES (%s,%s,%s, %s)
             """
    params = (userid,friend_id,content,date)

    settings.db_instance.execute_sql(sql, params)
