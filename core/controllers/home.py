#!/usr/bin/env python
#coding=utf-8
from flask import Flask, render_template, url_for, redirect, flash, request,jsonify
from flask.ext.wtf import Form, TextField,PasswordField, SubmitField, required, ValidationError

from core import app,db
from core.models import *
import json

@app.route('/', methods=['GET', 'POST'])
def index():
    b = Banshichu.query.all()  
    return render_template('index.html',Banshichu=b)


class LoginForm(Form):
    '''表单'''
    username = TextField(u"用户名", validators=[required(message=u"姓名不能为空")])
    password = PasswordField(u"密码", validators=[required(message=u"密码不能为空")])
    #verify = TextField(u"验证码", validators=[required(message=u"验证码不能为空")])
@app.route('/Login',methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        t = User.query.filter(User.UserName==form.username.data).filter(User.PassWord==form.password.data).first()  
        if t:
            flash(u"登录成功")
            return redirect(url_for('index'))
        else:
            flash(u"登录失败")
            return render_template('login.html',form=form)
    return render_template('login.html',form=form)

#ajax方法
@app.route('/api/shequ',methods=['GET', 'POST'])
def getShequ():
    s = Shequ.query.filter(Shequ.Banshichu_ID == request.args.get('banshichuId')).all()
    #return render_template('shequ.html',shequ=s)
    result =[]
    for t in s:
        shequ = {"ID":str(t.ID),"ShequName":t.ShequName}
        result.append(shequ)
    #print unicode(s[0].ShequName)
    return json.dumps(result, ensure_ascii=False)
    #print result
    #return  json.dumps(shequ, ensure_ascii=False)
    #return jsonify(json_list = list(s.all()))
    #return jsonify(result=10000)



"""
#申请
class ApplyForm(Form):
    '''表单'''
    username = TextField(u"用户名", validators=[required(message=u"姓名不能为空")])
    password = PasswordField(u"密码", validators=[required(message=u"密码不能为空")])
@app.route('/apply/create',methods=['GET','POST']
def applycreate():
    return render_template('login.html',form=form)
"""
