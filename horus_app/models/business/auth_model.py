from sqlalchemy import and_

from horus_app.models.basic_model import BasicModel
from horus_app.models.database.db_models import Department, Authority, Camera


class AuthModel(BasicModel):
    __page = 0
    __size = 0

    def __init__(self, page, size):
        BasicModel.__init__(self)
        self._response["data"] = {
            "total": 0,
            "auth": []
        }
        self.__page = page
        self.__size = size
        self._create_response()

    def _create_response(self):
        devices = self.__getAllAuth()
        self._response["data"]["total"], self._response["data"]["auth"] = \
            self._get_each_page_elements(devices, self.__page, self.__size)

    @staticmethod
    def __getAllAuth():
        authorities = []
        count = 1
        for auth_from_db in Authority.query.filter().all():
            user = {"id": count,
                    "department": Department.query.filter(
                        and_(Department.department_id ==
                             auth_from_db.department_id)).all()[0].department_name,
                    "camera": Camera.query.filter(
                        and_(Camera.camera_id ==
                             auth_from_db.camera_id)).all()[0].camera_name}
            count += 1
            authorities.append(user)
        return authorities
