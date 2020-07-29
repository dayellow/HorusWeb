from sqlalchemy import and_

from horus_app.models.basic_model import BasicModel
from horus_app.models.database.db_models import User, Department


class UserModel(BasicModel):
    __page = 0
    __size = 0

    def __init__(self, page, size):
        BasicModel.__init__(self)
        self._response["data"] = {
            "total": 0,
            "users": []
        }
        self.__page = page
        self.__size = size
        self._create_response()

    def _create_response(self):
        users = self.__getAllUsers()
        self._response["data"]["total"], self._response["data"]["users"] = \
            self._get_each_page_elements(users, self.__page, self.__size)

    @staticmethod
    def __getAllUsers():
        users = []
        count = 1
        for user_from_db in User.query.filter().all():
            user = {"id": count, "name": user_from_db.user_name,
                    "role": user_from_db.user_role,
                    "department": Department.query.filter(
                        and_(Department.department_id ==
                             user_from_db.department_id)).all()[0].department_name}
            users.append(user)
        return users
