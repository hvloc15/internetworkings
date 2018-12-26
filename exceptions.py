class MyException(Exception):
    status_code = None
    message = None

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message

class AuthenticationFailed(MyException):
    status_code = 401
    message = 'Incorrect authentication credentials'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message


class WrongInputType(MyException):
    status_code = 400
    message = 'Wrong input type'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message


class InsertError(MyException):
    status_code = 400
    message = 'Cannot insert into database'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message


class NotFoundError(MyException):
    status_code = 404
    message = 'Not found'

    def __init__(self, detail=None):
        self.message = detail or self.message

    def __str__(self):
        return self.message