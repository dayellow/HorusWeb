from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from horus_app.models.database.db_models import db
    db.init_app(app)

    from horus_app.views.apis import horus
    app.register_blueprint(horus)

    return app
