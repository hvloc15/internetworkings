from __future__ import unicode_literals
from datetime import datetime
import settings
import jwt
import time

def jwt_payload_handler(user):

    return {
        'user_id': user["pk"],
        'username': user["username"],
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    }


def jwt_get_user_id_from_payload_handler(payload):
    user_id = payload.get('user_id')
    return user_id


def jwt_encode_handler(payload):
    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM,
    ).decode('utf-8')


def jwt_decode_handler(token):
    options = {
        'verify_exp': settings.JWT_VERIFY_EXPIRATION,
    }
    
    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        settings.JWT_VERIFY,
        options=options,
        leeway=settings.JWT_LEEWAY
    )

user = {"pk":1,"username":2}
payload = jwt_payload_handler(user)
token = jwt_encode_handler(payload)
print(token)
time.sleep(2)
print(jwt_decode_handler(token))
