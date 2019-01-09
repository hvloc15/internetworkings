from functools import wraps

def annotate(tuple, list_key):
    return dict(zip(list_key, list(tuple)))

def ignore_client(view_func):
    @wraps(view_func)
    def wrapper(request, **kwargs):
        if kwargs.get('client') is not None:
            del kwargs['client']
        return view_func(request,**kwargs)

    return wrapper

