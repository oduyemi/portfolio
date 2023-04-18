from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin
from portfolio_app import db
#db=SQLAlchemy()



class Admin(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username=db.Column(db.String(30),nullable=True)
    admin_password=db.Column(db.String(200),nullable=True)


class Status(db.Model):
    status_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    status_name=db.Column(db.String(120),nullable=False)


class Msg(db.Model):
    msg_id=db.Column(db.Integer, autoincrement=True,primary_key=True) 
    msg_username=db.Column(db.String(150),nullable=False)   
    msg_email=db.Column(db.String(30),nullable=False)
    msg_subject=db.Column(db.String(200),nullable=False)
    msg_content=db.Column(db.Text(),nullable=False)
    msg_date = db.Column(db.DateTime(), default=datetime.utcnow)
    msg_status_id=db.Column(db.Integer, db.ForeignKey('status.status_id'))
    msg_admin=db.Column(db.Text(),nullable=True)

