from json_response import JsonResponse


class BaseView(object):
    permission_classes = ()

    def check_permissions(self, request):
        for permission_class in self.permission_classes:
            permission_instance = permission_class()
            if not permission_instance.validate(request):
                return JsonResponse(403, permission_instance.get_message()).as_json()
        return None

    def as_view(self, request):
        permission_check_message = self.check_permissions(request)
        if permission_check_message is not None:
            return permission_check_message
        try:
            self.view()
        except Exception as e:
            return JsonResponse(403, permission_instance.get_message()).as_json()

    def view(self):
        pass




