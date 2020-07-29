import json

from horus_app.models.basic_model import BasicModel


class Switch(BasicModel):
    __page = 0
    __size = 0

    def __init__(self, page, size):
        BasicModel.__init__(self)
        self._response["data"] = {
            "total": 0,
            "devices": []
        }
        self.__page = page
        self.__size = size
        self._create_response()

    def _create_response(self):
        devices = self.__getAllDevices()
        self._response["data"]["total"], self._response["data"]["nodes"] = \
            self._get_each_page_elements(devices, self.__page, self.__size)

    @staticmethod
    def __getAllDevices():
        switches = []

        with open("./fake_json_data/devices.json", "r") as devices_file:
            device_load_ret = json.load(devices_file)
            device_list = device_load_ret["devices"]
            count = 1
            for device in device_list:
                switch = {"id": count, "master": "", "status": "",
                          "cameranum": 0, "dpid": "", "type": "",
                          "version": "", "protocol": ""}
                count += 1
                if device["available"]:
                    switch["status"] = "ACTIVE"
                switch["dpid"] = device["id"]
                switch["type"] = device["hw"]
                switch["version"] = device["sw"]
                switch["protocol"] = device["annotations"]["protocol"]

                with open("./fake_json_data/masters.json", "r") as masters_file:
                    master_dict = json.load(masters_file)
                    node_list = master_dict["nodes"]
                    for node in node_list:
                        for device_ in node["devices"]:
                            if device_["id"] == device["id"]:
                                switch["master"] = node["id"]

                with open("./fake_json_data/hosts.json", "r") as hosts_file:
                    host_dict = json.load(hosts_file)
                    host_list = host_dict["hosts"]
                    for host in host_list:
                        if host["locations"][0]["elementId"] == device["id"]:
                            switch["cameranum"] += 1

                switches.append(switch)
        return switches
