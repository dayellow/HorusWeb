from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Camera(db.Model):
    __tablename__ = 'Camera'

    camera_id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.VARCHAR(50))
    camera_type = db.Column(db.VARCHAR(10))
    camera_ip = db.Column(db.VARCHAR(20))
    camera_longitude = db.Column(db.FLOAT)
    camera_latitude = db.Column(db.FLOAT)


class Department(db.Model):
    __tablename__ = "Department"

    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.VARCHAR(50))


class User(db.Model):
    __tablename__ = "User"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.VARCHAR(20))
    department_id = db.Column(db.Integer, db.ForeignKey('Department.department_id'))
    user_role = db.Column(db.VARCHAR(10))


class Authority(db.Model):
    __tablename__ = "Authority"

    camera_id = db.Column(db.Integer, db.ForeignKey('Camera.camera_id'), primary_key=True)
    department_id = db.Column(db.Integer,
                              db.ForeignKey('Department.department_id'), primary_key=True)
