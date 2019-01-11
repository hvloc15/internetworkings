from socket_project.views.base_view import BaseView
from socket_project.permissions.auth_permission import AuthPermission
from socket_project.json_response import JsonResponse
from socket_project.cache import cache


class Connection(BaseView):
    permission_classes = (AuthPermission,)

    def get(self, request, client):
        self.establish_connection(request, client)
        return JsonResponse(200, "Success", request).as_json()

    def establish_connection(self, request, client):
        username = request["User"]["username"]
        id = request["User"]["id"]
        client.username =  request["User"]["username"]
        client.id = id
        cache.set(username, client)
