import json


class JsonResponse:

    def __init__(self, status, message):
        self.status = status
        self.message = message

    def as_json(self):
        return json.dumps({
            "success": self.status,
            "message": self.message,
        })
