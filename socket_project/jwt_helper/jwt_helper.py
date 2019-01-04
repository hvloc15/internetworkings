from __future__ import unicode_literals
from datetime import datetime
from socket_project import settings
import jwt


def jwt_payload_handler(user):
    return {
        **user,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA,
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
