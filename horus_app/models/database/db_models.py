from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

authority = db.Table('Authority',
                     db.Column('camera_id', db.Integer,
                               db.ForeignKey('Camera.camera_id'), primary_key=True),
                     db.Column('department_id', db.Integer,
                               db.ForeignKey('Department.department_id'), primary_key=True)
                     )


class Camera(db.Model):
    __tablename__ = 'Camera'

    camera_id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.VARCHAR(50))
    camera_type = db.Column(db.VARCHAR(10))
    camera_ip = db.Column(db.VARCHAR(20))
    camera_longitude = db.Column(db.FLOAT)
    camera_latitude = db.Column(db.FLOAT)
    departments = db.relationship('Department', secondary=authority)


class Department(db.Model):
    __tablename__ = "Department"

    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.VARCHAR(50))
    cameras = db.relationship('Camera', secondary=authority)
