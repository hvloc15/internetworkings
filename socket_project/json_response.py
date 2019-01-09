import json


class JsonResponse:

    def __init__(self, status, message, request):
        self.status = status
        self.message = message
        self.request = request

    def as_json(self, error_message=False):
        response = {"status": self.status}

        if error_message:
            response["message"] = self.message
        else:
            response["data"] = self.message

        response["method"]= self.request["Method"]
        response["url"]= self.request["URL"]

        return json.dumps(response)
