from socket_project.views.base_view import BaseView
from socket_project.services.auth import login_service, signup_service
from socket_project.json_response import JsonResponse


class Auth(BaseView):

    def post(self, request, *args, **kwargs):
        function_name = request["URL"].split("/")[1]
        function = getattr(self, function_name.lower())
        return function(request)

    def login(self, request):
        body = request["DATA"]
        username = body["username"]
        password = body["password"]

        token = login_service(username, password)

        return JsonResponse(200, token).as_json()

    def signup(self, request):
        body = request["DATA"]
        username = body["username"]
        password = body["password"]
        date_of_birth = body["dateofbirth"]

        signup_service(username,password,date_of_birth)

        return JsonResponse(201, "Created").as_json()
    