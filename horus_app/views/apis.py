import json

from flask_restful import Resource, Api
from flask import Blueprint

from horus_app.models.database.db_models import *

horus = Blueprint('horus', __name__)
api = Api(horus)


class DashBoard(Resource):
    response = {
        "code": 200,
        "msg": "success",
        "data": {
            "controllernum": 0,
            "switchnum": 0,
            "cameranum": 0,
            "memper": 0,
            "switchper": 0,
            "cameraper": 0,
            "cameras": []
        }
    }

    def get(self):
        self.response["data"]["controllernum"] = self._getControllerNum()
        self.response["data"]["switchnum"], self.response["data"]["switchper"] = \
            self._getSwitchNum()
        self.response["data"]["cameranum"], self.response["data"]["cameraper"] = \
            self._getCameraNum()
        self.response["data"]["memper"] = self._getMemoryPer()
        self.response["data"]["cameras"] = self._getCamerasInMap()
        return self.response

    # 获取控制器数量
    @staticmethod
    def _getControllerNum():
        with open("./fake_json_data/cluster.json", "r") as f:
            load_dict = json.load(f)
            node_list = load_dict["nodes"]
            return len(node_list)

    # 获取在线交换机数量和在线率
    @staticmethod
    def _getSwitchNum():
        switch_online_num = 0
        with open("./fake_json_data/devices.json", "r") as f:
            load_dict = json.load(f)
            device_list = load_dict["devices"]
            for device in device_list:
                if device["available"]:
                    switch_online_num += 1
            return switch_online_num, int(switch_online_num / len(device_list) * 100)

    # 获取在线摄像头数量和在线率
    @staticmethod
    def _getCameraNum():
        with open("./fake_json_data/hosts.json", "r") as f:
            load_dict = json.load(f)
            host_list = load_dict["hosts"]
            camera_online_num = len(host_list)

        return camera_online_num, int(len(Camera.query.filter().all())
                                      / camera_online_num * 100)

    # 获取内存使用率
    @staticmethod
    def _getMemoryPer():
        with open("./fake_json_data/system.json", "r") as f:
            load_dict = json.load(f)
            mem = load_dict["mem"]
            return int(mem["current"] / mem["max"] * 100)

    # 获取地图里的摄像头信息
    @staticmethod
    def _getCamerasInMap():
        camera_json_object = {}
        cameras_all = []
        ip_online_list = []

        with open("./fake_json_data/hosts.json", "r") as f:
            load_dict = json.load(f)
            host_list = load_dict["hosts"]
            for host in host_list:
                ip_online_list.append(host["ipAddresses"][0])

        for camera in Camera.query.filter().all():
            camera_json_object["longitude"] = camera.camera_longitude
            camera_json_object["latitude"] = camera.camera_latitude
            if camera.camera_ip in ip_online_list:
                camera_json_object["status"] = "online"
            else:
                camera_json_object["status"] = "offline"
            cameras_all.append(camera_json_object)

        return cameras_all


class Controller(Resource):
    response = {
        "code": 200,
        "msg": "success",
        "data": {
            "nodes": []
        }
    }

    def get(self):
        self.response["data"]["nodes"] = self._getAllController()
        return self.response

    @staticmethod
    def _getAllController():
        controllers = []

        with open("./fake_json_data/cluster.json", "r") as cluster:
            cluster_dict = json.load(cluster)
            count = 1
            for node in cluster_dict["nodes"]:
                controller = {"id": count, "name": "", "ip": "", "status": "",
                              "deviceNum": 0, "tcpPort": 0}

                count += 1

                controller["name"] = node["id"]
                controller["ip"] = node["ip"]
                controller["status"] = node["status"]
                controller["tcpPort"] = node["tcpPort"]

                with open("./fake_json_data/masters.json", "r") as master:
                    master_dict = json.load(master)
                    for node_ in master_dict["nodes"]:
                        if node_["id"] == node["id"]:
                            controller["deviceNum"] = len(node_["devices"])

                print(controller)
                controllers.append(controller)
                print(controllers)
            print(controllers)
            return controllers


class Switch(Resource):
    response = {
        "code": 200,
        "msg": "success",
        "data": {
            "devices": []
        }
    }

    def get(self):
        self.response["data"]["devices"] = self._getAllSwitch()
        return self.response

    @staticmethod
    def _getAllSwitch():
        switches = []

        with open("./fake_json_data/devices.json", "r") as deviceFile:
            device_dict = json.load(deviceFile)
            device_list = device_dict["devices"]
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

                with open("./fake_json_data/masters.json", "r") as masterFile:
                    master_dict = json.load(masterFile)
                    node_list = master_dict["nodes"]
                    for node in node_list:
                        for device_ in node["devices"]:
                            if device_["id"] == device["id"]:
                                switch["master"] = node["id"]

                with open("./fake_json_data/hosts.json", "r") as hostFile:
                    host_dict = json.load(hostFile)
                    host_list = host_dict["hosts"]
                    for host in host_list:
                        if host["locations"][0]["elementId"] == device["id"]:
                            switch["cameranum"] += 1

                switches.append(switch)
        return switches


api.add_resource(DashBoard, '/dashboard/statistic')
api.add_resource(Controller, '/controller/info')
api.add_resource(Switch, "/device/info")
