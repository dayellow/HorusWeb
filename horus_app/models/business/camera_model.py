import json

from horus_app.models.basic_model import BasicModel
from horus_app.models.database.db_models import Camera


class CameraModel(BasicModel):
    __page = 0
    __size = 0

    def __init__(self, page, size):
        BasicModel.__init__(self)
        self._response["data"] = {
            "total": 0,
            "cameras": []
        }
        self.__page = page
        self.__size = size
        self._create_response()

    def _create_response(self):
        cameras = self.__getAllCameras()
        self._response["data"]["total"], self._response["data"]["cameras"] = \
            self._get_each_page_elements(cameras, self.__page, self.__size)

    @staticmethod
    def __getAllCameras():
        cameras = []
        ip_online = []

        with open("./fake_json_data/hosts.json", "r") as hosts_file:
            hosts_load_ret = json.load(hosts_file)
            hosts = hosts_load_ret["hosts"]
            for host in hosts:
                ip_online.append(host["ipAddresses"][0])

        count = 1
        for camera_ in Camera.query.filter().all():
            camera = {"id": count}
            count += 1
            camera["name"] = camera_.camera_name
            camera["type"] = camera_.camera_type
            camera["ip"] = camera_.camera_ip
            camera["longitude"] = camera_.camera_longitude
            camera["latitude"] = camera_.camera_latitude
            if camera_.camera_ip in ip_online:
                camera["status"] = "online"
            else:
                camera["status"] = "offline"
            cameras.append(camera)

        return cameras
