#!/usr/bin/env python
#coding=utf-8
from core import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class Banshichu(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    BanshichuName = db.Column(db.String(50))
    BanshichuCode = db.Column(db.String(5))
    Shequs=db.relationship('Shequ',backref='banshichu',lazy='dynamic')

    def __init__(self,*args,**kwargs):
        super(Banshichu,self).__init__(*args,**kwargs)
    def __repr__(self):
        return "Banshichu %s" % self.BanshichuName

class Shequ(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    ShequName = db.Column(db.String(50))
    Banshichu_ID = db.Column(db.Integer,db.ForeignKey('banshichu.ID'))
    ShequCode = db.Column(db.String(5))

    def __init__(self,*args,**kwargs):
        super(Shequ,self).__init__(*args,**kwargs)
    def __repr__(self):
        #return "ShequName %s" % self.ShequName
        return "<Shequ('%s','%s')>" % (self.ShequName, self.ShequCode)
    def to_json(self):
        return {
            'ID': self.ID,
            'ShequName': self.ShequName,
            #'time': Date.unix_to_human(self.create_time),
        }


    

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    UserName = db.Column(db.String(255),nullable=False)
    PassWord = db.Column(db.String(255),nullable=False)
    Banshichu_ID = db.Column(db.Integer,db.ForeignKey('banshichu.ID'))
    Shequ_ID = db.Column(db.Integer,db.ForeignKey('shequ.ID'))

    def __init__(self,*args,**kwargs):
        super(User,self).__init__(*args,**kwargs)
    def __repr__(self):
        return "User %s" % self.name

    def store_to_db(self):
        '''保存数据到数据库'''
        
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        '''删除数据'''
        
        db.session.delete(self)
        db.session.commit()

    def validate_name(form, field):
        if field.data == 0:
            raise ValidationError, u'内容不能为空'

class Apply(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    SerialNumber=db.Column(db.String(255))
