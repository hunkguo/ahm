#!/usr/bin/env python
#coding=utf-8
from core import manager, db

if __name__ == '__main__':
    db.create_all()
    manager.run()