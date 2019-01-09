from socket_project.views.base_view import BaseView
from socket_project.services.blog import create_blog_service
from socket_project.json_response import JsonResponse
from socket_project.permissions.auth_permission import AuthPermission


class Blog(BaseView):
    permission_classes = (AuthPermission,)

    def post(self, request):
        body = request["DATA"]
        userid = request["User"]["id"]
        content = body["content"]
        date = body["date"]

        create_blog_service(userid, content, date)

        return JsonResponse(200, "Success", request).as_json()
    