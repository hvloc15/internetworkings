import datetime

SECRET_KEY = 'u4t!0=7ujtj5e$#g&t%swpbp!q#7y70f%(rz$+79%0o%ta$gow'

HOST = "127.0.0.1"
PORT = 65432
NUMBER_OF_CONNECTION = 5

DB_CONFIG = {
    "host": "localhost",
    "database": "socket_db",
    "user": "root",
    "password": "1011988"
}

JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=86400)
JWT_SECRET_KEY = 'u4t!0=7ujtj5e$#g&t%swpbp!q#7y70f%(rz$+79%0o%ta$gow'
JWT_ALGORITHM = "HS256"
JWT_VERIFY_EXPIRATION = True
JWT_VERIFY = True
JWT_LEEWAY = 0

# message = {
#     "METHOD": "GET/POST",
#     "URL": "API/url",
#     "AUTHORIZATION"
#     "DATA":{
#         "a": 1,
#         "b": 2
#     }
# }