import json

from flask_restful import Resource, Api, reqparse
from flask import Blueprint

from horus_app.models.business.camera_model import CameraModel
from horus_app.models.business.controller_model import ControllerModel
from horus_app.models.business.dash_board_model import DashBoardModel
from horus_app.models.business.switch_model import SwitchModel
from horus_app.models.database.db_models import *

horus = Blueprint('horus', __name__)
api = Api(horus)


class DashBoardApi(Resource):

    @staticmethod
    def get():
        dashboard_model = DashBoardModel()
        return dashboard_model.get_response()


class ControllerApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        controller_model = ControllerModel(page=page, size=size)
        return controller_model.get_response()


class SwitchApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        switch_model = SwitchModel(page=page, size=size)
        return switch_model.get_response()


class CameraApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        camera_model = CameraModel(page=page, size=size)
        return camera_model.get_response()


api.add_resource(DashBoardApi, '/dashboard/statistic')
api.add_resource(ControllerApi, '/controller/info')
api.add_resource(SwitchApi, '/device/info')
api.add_resource(CameraApi, '/camera/info')
