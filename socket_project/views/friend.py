from socket_project.views.base_view import BaseView
from socket_project.services.friend import get_list_friend_service, \
    accept_friend_service, add_friend_service, cancle_friend_request_service
from socket_project.json_response import JsonResponse
from socket_project.permissions.auth_permission import AuthPermission
from socket_project.exceptions import BadRequest


class Friend(BaseView):
    permission_classes = (AuthPermission, )

    def get(self, request, friendid = None):
        if friendid is None:
            user = get_list_friend_service(request)
            return JsonResponse(200, user).as_json()

    def post(self, request):
        function_name = request["URL"].split('/')[1]
        func = getattr(self,function_name)
        try:
            friendid = request["DATA"]["id"]
            return func(request, friendid)
        except:
            raise BadRequest("Invalid body format")

    def accept(self, request, friendid):
        accept_friend_service(request["User"]["id"], friendid)
        return JsonResponse(200, "Success").as_json()

    def add(self, request, friendid):
        add_friend_service(request["User"]["id"], friendid)
        return JsonResponse(200, "Success").as_json()

    def cancle(self, request, friendid):
        cancle_friend_request_service(request["User"]["id"], friendid)
        return JsonResponse(200, "Success").as_json()
