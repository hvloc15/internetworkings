from socket_project.exceptions import AuthenticationFailed
from socket_project.jwt_helper.jwt_helper import jwt_decode_handler


class AuthPermission:

    def validate(self, request):
        token = request.get("Authorization")
        if token is None:
            raise AuthenticationFailed("No authentication header provided")
        try:
            payload = jwt_decode_handler(token)
            request["User"] = {
                "id": payload.get("id"),
                "username": payload.get("username")
            }
        except Exception as e:
            raise AuthenticationFailed(str(e))
