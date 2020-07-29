from horus_app.models.basic_model import BasicModel


class DashBoard(BasicModel):
    def __init__(self):
        BasicModel.__init__(self)
        self._response["data"] = {

        }
