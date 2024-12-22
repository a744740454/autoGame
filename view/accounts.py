#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：autoGameScript 
@File    ：accounts.py
@Author  ：sadnesspineapple
@Date    ：2024/12/22 16:34 
'''
# built-in package
from models import GameAccount
from flask import request, jsonify


# project package

# third package

@app.route('/gameaccounts', methods=['GET'])
def get_game_accounts():
    accounts = GameAccount.query.all()
    return jsonify([account.to_dict() for account in accounts])


# Route to get a specific game account by ID
@app.route('/gameaccounts/<int:id>', methods=['GET'])
def get_game_account(id):
    account = GameAccount.query.get(id)
    if account:
        return jsonify(account.to_dict())
    else:
        return jsonify({'error': 'Game account not found'}), 404


# Route to create a new game account
@app.route('/gameaccounts', methods=['POST'])
def create_game_account():
    data = request.get_json()
    if not data or not all(k in data for k in ['userId', 'password', 'status', 'gameType']):
        return jsonify({'error': 'Missing required fields'}), 400

    new_account = GameAccount(
        userId=data['userId'],
        password=data['password'],
        status=data['status'],
        workType=data.get('workType'),
        gameType=data['gameType'],
        data=data.get('data')
    )

    db.session.add(new_account)
    db.session.commit()

    return jsonify(new_account.to_dict()), 201


# Route to update an existing game account
@app.route('/gameaccounts/<int:id>', methods=['PUT'])
def update_game_account(id):
    data = request.get_json()
    account = GameAccount.query.get(id)

    if not account:
        return jsonify({'error': 'Game account not found'}), 404

    account.userId = data.get('userId', account.userId)
    account.password = data.get('password', account.password)
    account.status = data.get('status', account.status)
    account.workType = data.get('workType', account.workType)
    account.gameType = data.get('gameType', account.gameType)
    account.data = data.get('data', account.data)

    db.session.commit()

    return jsonify(account.to_dict())


# Route to delete a game account
@app.route('/gameaccounts/<int:id>', methods=['DELETE'])
def delete_game_account(id):
    account = GameAccount.query.get(id)
    if not account:
        return jsonify({'error': 'Game account not found'}), 404

    db.session.delete(account)
    db.session.commit()

    return jsonify({'message': 'Game account deleted successfully'})
