from socket_project.db.db import Db
from socket_project import settings

db_instance = Db(**settings.DB_CONFIG)
cache = {}
