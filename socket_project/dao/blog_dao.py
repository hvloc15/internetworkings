import settings
from socket_project.utils.utils import annotate


def create_blog(userid, content, date):
    sql = """INSERT INTO blog (userid, content, date)
             VALUES (%s,%s,%s)
               """
    settings.db_instance.execute_sql(sql, (userid, content,date))


def get_list_blog(friend_ids, page, page_size):

    offset = int(page) * int(page_size)
    limit = int(page_size)

    format_strings = ','.join(['%s'] * len(friend_ids))
    sql = """
        SELECT blog.userid, blog.content, blog.date
        FROM blog
        WHERE blog.userid IN({list})
        ORDER BY date DESC
        LIMIT %s,%s
    """
    params = [*friend_ids, offset, limit]
    records = settings.db_instance.query(sql.format(list = format_strings), params)
    if records is None:
        return []
    result = [annotate(record, ("id", "content", "date")) for record in records]
    print("Blog: ", result)
    return result


#get_list_blog([1,2,5],0, page_size=20)