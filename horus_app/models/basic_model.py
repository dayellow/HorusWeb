class BasicModel(object):
    _response = {}

    def __init__(self):
        self._response = {
            "code": 200,
            "msg": "success",
            "data": {}
        }

    def _create_response(self):
        pass

    def get_response(self):
        return self._response

    @staticmethod
    def _get_each_page_elements(complete_list, page, size):
        if len(complete_list) % size != 0:
            total = len(complete_list) // size + 1
        else:
            total = len(complete_list) // size
        start_index = (page - 1) * size
        end_index = page * size
        intercepted_list = complete_list[start_index: end_index]
        return total, intercepted_list
