from socket_project.views.base_view import BaseView
from socket_project.services.user import get_user_service
from socket_project.json_response import JsonResponse
from socket_project.permissions.auth_permission import AuthPermission


class User(BaseView):
    permission_classes = (AuthPermission,)

    def get(self, request, id = None):
        if id is not None:
            user = get_user_service(id)
            return JsonResponse(200, user).as_json()
