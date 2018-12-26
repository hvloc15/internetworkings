from json_response import JsonResponse
from exceptions import MyException


class BaseView(object):
    permission_classes = ()

    def check_permissions(self, request):
        for permission_class in self.permission_classes:
            permission_instance = permission_class()
            permission_instance.validate(request)

    def as_view(self, request, **kwargs):
        self.check_permissions(request)
        return self.view(request,**kwargs)


    def view(self,request, **kwargs):
        pass
