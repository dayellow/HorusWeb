import json

from horus_app.models.basic_model import BasicModel
from horus_app.models.database.db_models import Camera


class DashBoardModel(BasicModel):

    def __init__(self):
        BasicModel.__init__(self)
        self._response["data"] = {
            "controllernum": 0,
            "switchnum": 0,
            "cameranum": 0,
            "memper": 0,
            "switchper": 0,
            "cameraper": 0,
            "cameras": []
        }
        self._create_response()

    def _create_response(self):
        self._response["data"]["controllernum"] = self.__getControllerNum()
        self._response["data"]["switchnum"], self._response["data"]["switchper"] = \
            self.__getSwitchNum()
        self._response["data"]["cameranum"], self._response["data"]["cameraper"] = \
            self.__getCameraNum()
        self._response["data"]["memper"] = self.__getMemoryPer()
        self._response["data"]["cameras"] = self.__getCamerasInMap()

    @staticmethod
    def __getControllerNum():
        with open("./fake_json_data/cluster.json", "r") as cluster_file:
            cluster_load_ret = json.load(cluster_file)
            nodes = cluster_load_ret["nodes"]
            return len(nodes)

    @staticmethod
    def __getSwitchNum():
        switch_online_num = 0
        with open("./fake_json_data/devices.json", "r") as device_file:
            device_load_ret = json.load(device_file)
            devices = device_load_ret["devices"]
            for device in devices:
                if device["available"]:
                    switch_online_num += 1
            return switch_online_num, int(switch_online_num / len(devices) * 100)

    @staticmethod
    def __getCameraNum():
        with open("./fake_json_data/hosts.json", "r") as hosts_file:
            host_load_ret = json.load(hosts_file)
            hosts = host_load_ret["hosts"]
            camera_online_num = len(hosts)

        return camera_online_num, int(len(Camera.query.filter().all())
                                      / camera_online_num * 100)

    @staticmethod
    def __getMemoryPer():
        with open("./fake_json_data/system.json", "r") as system_file:
            system_load_ret = json.load(system_file)
            mem = system_load_ret["mem"]
            return int(mem["current"] / mem["max"] * 100)

    @staticmethod
    def __getCamerasInMap():
        camera_on_map = {}
        cameras = []
        ip_online = []

        with open("./fake_json_data/hosts.json", "r") as hosts_file:
            hosts_load_ret = json.load(hosts_file)
            hosts = hosts_load_ret["hosts"]
            for host in hosts:
                ip_online.append(host["ipAddresses"][0])

        for camera in Camera.query.filter().all():
            camera_on_map["longitude"] = camera.camera_longitude
            camera_on_map["latitude"] = camera.camera_latitude
            if camera.camera_ip in ip_online:
                camera_on_map["status"] = "online"
            else:
                camera_on_map["status"] = "offline"
            cameras.append(camera_on_map)

        return cameras
