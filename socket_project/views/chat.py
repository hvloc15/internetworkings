from socket_project.views.base_view import BaseView
from socket_project.services.chat import get_list_message_service, notify_typing_service, send_message_service
from socket_project.json_response import JsonResponse
from socket_project.permissions.auth_permission import AuthPermission
from socket_project.exceptions import BadRequest


class Chat(BaseView):
    permission_classes = (AuthPermission, )

    def get(self, request, client=None, friendid = None):
        if friendid is not None:
            message = get_list_message_service(request, friendid)
            return JsonResponse(200, message, request).as_json()

    def post(self, request, client, friendid = None):
        function_name = request["URL"].split('/')[1]
        func = getattr(self,function_name)
        if friendid is None:
            try:
                return func(request)
            except:
                raise BadRequest("Invalid body format")

    def istyping(self, request):
        body = request["DATA"]
        friend_username = body["username"]

        notify_typing_service(request, friend_username)
        return JsonResponse(200, "notified", request)

    def send(self, request):
        send_message_service(request)
        return JsonResponse(200, "created", request)