import json


class JsonResponse:

    def __init__(self, status, message, request=None):
        self.status = status
        self.message = message
        if request is not None:
            self.request = request

    def as_json(self, error_message=False):
        response = {"status": self.status}

        if error_message:
            response["message"] = self.message
        else:
            response["data"] = self.message

        if self.request is not None:
            response["method"]= self.request["Method"]
            response["url"]= self.request["URL"]

        return json.dumps(response)
