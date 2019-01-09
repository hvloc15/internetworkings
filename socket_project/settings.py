import datetime

SECRET_KEY = 'u4t!0=7ujtj5e$#g&t%swpbp!q#7y70f%(rz$+79%0o%ta$gow'

HOST = "172.16.22.23"
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

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

WEBSOCKET_ANSWER = (
    'HTTP/1.1 101 Switching Protocols',
    'Upgrade: websocket',
    'Connection: Upgrade',
    'Sec-WebSocket-Accept: {key}\r\n\r\n',
)
