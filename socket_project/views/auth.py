from socket_project.views.base_view import BaseView
from socket_project.services.auth import login_service, signup_service
from socket_project.json_response import JsonResponse
import settings


class Auth(BaseView):

    def post(self, request, client):
        function_name = request["URL"].split("/")[1]
        function = getattr(self, function_name.lower())
        return function(request, client)

    def login(self, request, client):
        body = request["DATA"]
        username = body["username"]
        password = body["password"]

        token = login_service(username, password, client)

        return JsonResponse(200, token, request).as_json()

    def signup(self, request):
        body = request["DATA"]
        username = body["username"]
        password = body["password"]
        date_of_birth = body["dateofbirth"]

        signup_service(username,password,date_of_birth)

        return JsonResponse(201, "Created", request).as_json()
    