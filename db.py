from mysql.connector import Error
from mysql.connector import pooling


def create_connection_pool(dbconfig, pool_size=20, pool_name="mypool"):
    """ Connect to MySQL database """
    try:
        connection_pool = pooling.MySQLConnectionPool(pool_name=pool_name,
                                                      pool_size=pool_size,
                                                      **dbconfig,
                                                      )
        return connection_pool
    except Error as e:
        print(e)
        return None


def query(connection, sql, params=()):
    try:
        mycursor = connection.cursor()
        mycursor.execute(sql, params=params)

        result = mycursor.fetchall()

        if len(result) == 1:
            return result[0]
        return result
    except Error as e:
        print(e)
    finally:
        mycursor.close()
        connection.close()


def insert(connection, sql, params=()):
    try:
        mycursor = connection.cursor()
        mycursor.execute(sql, params=params)
        mycursor.commit()
    except Error as error:
        print(error)
    finally:
        mycursor.close()
        connection.close()
