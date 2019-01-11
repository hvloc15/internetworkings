from socket_project.views.base_view import BaseView
from socket_project.services.blog import create_blog_service, get_list_blog_service
from socket_project.json_response import JsonResponse
from socket_project.permissions.auth_permission import AuthPermission


class Blog(BaseView):
    permission_classes = (AuthPermission,)

    def post(self, request, client):
        create_blog_service(request)

        return JsonResponse(200, "Success", request).as_json()

    def get(self, request, client=None):
        message = get_list_blog_service(request)
        return JsonResponse(200, message, request).as_json()
