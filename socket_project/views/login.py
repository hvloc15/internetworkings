from socket_project.views.base_view import BaseView
from socket_project.services.auth import login_service
from socket_project.json_response import JsonResponse


class Login(BaseView):

    def post(self, request, *args, **kwargs):
        body = request["DATA"]
        username = body["username"]
        password = body["password"]

        token = login_service(username, password)

        return JsonResponse(200, token).as_json()
