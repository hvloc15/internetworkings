import json


class JsonResponse:

    def __init__(self, status, message):
        self.status = status
        self.message = message

    def as_json(self, error_message=False):
        response = {"status": self.status}

        if error_message:
            response["message"] = self.message
        else:
            response["data"] = self.message

        return json.dumps(response)
