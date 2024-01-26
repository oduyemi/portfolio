from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from portfolio_app import config
# from flask_mail import Mail, Message


starter = Flask(__name__,instance_relative_config=True)
starter.config.from_pyfile('config.py', silent=False)

db = SQLAlchemy(starter)



from portfolio_app import adminroutes,userroutes