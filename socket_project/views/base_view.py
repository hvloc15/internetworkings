from socket_project.exceptions import MethodNotAllowedError


class BaseView(object):
    permission_classes = ()
    method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def check_permissions(self, request):
        for permission_class in self.permission_classes:
            permission_instance = permission_class()
            permission_instance.validate(request)

    @classmethod
    def as_view(cls,):
        def view_func(request, *args, **kwargs):
            self = cls()
            self.check_permissions(request)
            return self.dispatch(request, *args, **kwargs)

        return view_func

    def dispatch(self, request, *args, **kwargs):
        if request["Method"].lower() in self.method_names:
            handler = getattr(self, request["Method"].lower(), self.method_not_allowed)
        else:
            handler = self.method_not_allowed
        return handler(request, *args, **kwargs)

    def method_not_allowed(self, request, *args, **kwargs):
        raise MethodNotAllowedError(method=request["Method"])