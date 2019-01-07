from mysql.connector import Error
from mysql.connector import pooling


class Db:
    def __init__(self, **kwargs):
        self.pool = self.create_connection_pool(kwargs)
        print("HUHUHU")

    def create_connection_pool(self, dbconfig, pool_size=20, pool_name="mypool"):
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

    def query(self, sql, params=()):
        try:
            connection = self.pool.get_connection()
            mycursor = connection.cursor()
            mycursor.execute(sql, params=params)

            result = mycursor.fetchall()
            if len(result) == 0:
                return None
            return result
        except Error as e:
            raise Error
        finally:
            mycursor.close()
            connection.close()

    def execute_sql(self, sql, params=()):
        try:
            connection = self.pool.get_connection()
            mycursor = connection.cursor()
            mycursor.execute(sql, params=params)
            connection.commit()
        except Error as error:
            raise Error
        finally:
            mycursor.close()
            connection.close()
