class BasicModel(object):
    _response = {}

    def __init__(self):
        self._response = {
            "code": 200,
            "msg": "success",
            "data": {}
        }

    def get_response(self):
        return self._response