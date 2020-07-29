import json

from flask_restful import Resource, Api, reqparse
from flask import Blueprint

from horus_app.models.business.controller import Controller
from horus_app.models.business.dash_board import DashBoard
from horus_app.models.business.switch import Switch
from horus_app.models.database.db_models import *

horus = Blueprint('horus', __name__)
api = Api(horus)


class DashBoardApi(Resource):

    @staticmethod
    def get():
        dashboard = DashBoard()
        return dashboard.get_response()


class ControllerApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        controller = Controller(page=page, size=size)
        return controller.get_response()


class SwitchApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        page = parser.parse_args()["page"]
        size = parser.parse_args()["size"]
        switch = Switch(page=page, size=size)
        return switch.get_response()


api.add_resource(DashBoardApi, '/dashboard/statistic')
api.add_resource(ControllerApi, '/controller/info')
api.add_resource(SwitchApi, "/device/info")
