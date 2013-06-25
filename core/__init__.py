#!/usr/bin/env python
#coding=utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager

DEBUG = True


app = Flask(__name__)
app.config.from_object('core.config')
app.config["SQLALCHEMY_ECHO"] = True
app.debug = True
db = SQLAlchemy(app)
db.init_app(app)



from core.models import User,Shequ,Banshichu
from core.controllers import *





manager = Manager(app)

@manager.command
def createall():
    '''创建数据库'''
    db.create_all()

@manager.command
def dropall():
    '''清除数据'''
    db.drop_all()

if __name__ == '__main__':
    manager.run(debug=true)
