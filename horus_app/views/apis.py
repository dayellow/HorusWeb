from flask import Blueprint
from flask_restful import Resource, Api, reqparse

from horus_app.models.business.auth_model import AuthModel
from horus_app.models.business.camera_model import CameraModel
from horus_app.models.business.controller_model import ControllerModel
from horus_app.models.business.dash_board_model import DashBoardModel
from horus_app.models.business.switch_model import SwitchModel
from horus_app.models.business.user_model import UserModel

horus = Blueprint('horus', __name__)
api = Api(horus)


class DashBoardStatisticApi(Resource):

    @staticmethod
    def get():
        dashboard_model = DashBoardModel()
        return dashboard_model.get_response()


class ControllerInfoApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        controller_model = ControllerModel(page=page, size=size)
        return controller_model.get_response()


class DeviceInfoApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        switch_model = SwitchModel(page=page, size=size)
        return switch_model.get_response()


class CameraInfoApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        camera_model = CameraModel(page=page, size=size)
        return camera_model.get_response()


class CameraEditApi(Resource):
    @staticmethod
    def put():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class CameraDeleteApi(Resource):
    @staticmethod
    def delete():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class CameraAddApi(Resource):
    @staticmethod
    def post():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class UserInfoApi(Resource):
    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        user_model = UserModel(page=page, size=size)
        return user_model.get_response()


class UserEditApi(Resource):
    @staticmethod
    def put():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class UserDeleteApi(Resource):
    @staticmethod
    def delete():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class UserAddApi(Resource):
    @staticmethod
    def post():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class AuthInfoApi(Resource):
    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        role_model = AuthModel(page=page, size=size)
        return role_model.get_response()


class AuthEditApi(Resource):
    @staticmethod
    def put():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class AuthDeleteApi(Resource):
    @staticmethod
    def delete():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


class AuthAddApi(Resource):
    @staticmethod
    def post():
        return {"code": 300, "msg": "该账号权限不足", "data": {}}


api.add_resource(DashBoardStatisticApi, '/dashboard/statistic')
api.add_resource(ControllerInfoApi, '/controller/info')
api.add_resource(DeviceInfoApi, '/device/info')
api.add_resource(CameraInfoApi, '/camera/info')
api.add_resource(CameraEditApi, '/camera/edit')
api.add_resource(CameraDeleteApi, '/camera/delete')
api.add_resource(CameraAddApi, '/camera/add')
api.add_resource(UserInfoApi, '/user/info')
api.add_resource(UserEditApi, '/user/edit')
api.add_resource(UserDeleteApi, '/user/delete')
api.add_resource(UserAddApi, '/user/add')
api.add_resource(AuthInfoApi, '/auth/info')
api.add_resource(AuthEditApi, '/auth/edit')
api.add_resource(AuthDeleteApi, '/auth/delete')
api.add_resource(AuthAddApi, '/auth/add')
