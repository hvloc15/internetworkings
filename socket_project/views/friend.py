from socket_project.views.base_view import BaseView
from socket_project.services.friend import get_list_friend_service, \
    accept_friend_service, add_friend_service, cancle_friend_request_service
from socket_project.json_response import JsonResponse
from socket_project.permissions.auth_permission import AuthPermission
from socket_project.exceptions import BadRequest


class Friend(BaseView):
    permission_classes = (AuthPermission, )

    def get(self, request,client=None, friendid = None):
        if friendid is None:
            user = get_list_friend_service(request)
            return JsonResponse(200, user, request).as_json()

    def post(self, request, client= None):
        function_name = request["URL"].split('/')[1]
        func = getattr(self,function_name)
        try:
            friend_id = request["DATA"]["id"]
            return func(request, friend_id)

        except:
            raise BadRequest("Invalid body format")

    def accept(self, request, friend_id, client= None):
        user = accept_friend_service(request["User"]["id"], friend_id)
        return JsonResponse(200, user, request).as_json()

    def add(self, request, friend_username, client= None):
        user = add_friend_service(request, friend_username)
        return JsonResponse(200, user, request).as_json()

    def cancle(self, request, friend_username, client= None):
        cancle_friend_request_service(request["User"]["id"], friend_username)
        return JsonResponse(200, "Success", request).as_json()
