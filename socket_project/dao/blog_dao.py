import settings


def create_blog(userid, content, date):
    sql = """INSERT INTO blog (userid, content, date)
             VALUES (%s,%s,%s)
               """
    settings.db_instance.execute_sql(sql, (userid, content,date))
