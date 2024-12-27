1#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：autoGameScript 
@File    ：__init__.py
@Author  ：sadnesspineapple
@Date    ：2024/12/22 16:33 
'''
# built-in package

# project package

# third package
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class GameAccount(db.Model):
    __tablename__ = 'gameAccounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.DateTime, default=db.func.current_timestamp())
    workType = db.Column(db.String(255))
    gameType = db.Column(db.String(255), nullable=False)
    data = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'account': self.account,
            'password': self.password,
            'status': self.status,
            'datetime': self.datetime,
            'workType': self.workType,
            'gameType': self.gameType,
            'data': self.data
        }

class IdCard(db.Model):
    __tablename__ = 'idCard'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_number = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(16), nullable=False)
    status = db.Column(db.String(1), nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'card_number': self.card_number,
            'name': self.name,
            'status': self.status
        }
