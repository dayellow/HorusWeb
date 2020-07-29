import json

from horus_app.models.basic_model import BasicModel


class Controller(BasicModel):
    __page = 0
    __size = 0

    def __init__(self, page, size):
        BasicModel.__init__(self)
        self._response["data"] = {
            "total": 0,
            "nodes": []
        }
        self.__page = page
        self.__size = size
        self._create_response()

    def _create_response(self):
        controllers = self.__getAllController()
        self._response["data"]["total"], self._response["data"]["nodes"] = \
            self._get_each_page_elements(controllers, self.__page, self.__size)

    @staticmethod
    def __getAllController():
        controllers = []

        with open("./fake_json_data/cluster.json", "r") as cluster_file:
            cluster_load_ret = json.load(cluster_file)
            count = 1
            for node in cluster_load_ret["nodes"]:
                controller = {"id": count, "name": "", "ip": "", "status": "",
                              "deviceNum": 0, "tcpPort": 0}

                count += 1

                controller["name"] = node["id"]
                controller["ip"] = node["ip"]
                controller["status"] = node["status"]
                controller["tcpPort"] = node["tcpPort"]

                with open("./fake_json_data/masters.json", "r") as masters_file:
                    master_load_ret = json.load(masters_file)
                    for node_ in master_load_ret["nodes"]:
                        if node_["id"] == node["id"]:
                            controller["deviceNum"] = len(node_["devices"])

                controllers.append(controller)
            return controllers
