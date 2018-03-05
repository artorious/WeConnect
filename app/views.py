#!/usr/bin/env python3
""" Routes for app. Tells lask what to display on which path """

from flask import request, jsonify
from app.models import WeConnect
from app import app

@app.route('/v1/', methods=['GET'])
def index(): 
    """ Return method made by the user to request resource """
    return jsonify(request.method)
    
@app.route('/v1/register/', methods=['POST'])
def register_user():
    """ Creates a user account """
    user = WeConnect()
    
    data= request.get_json()
    response = user.create_user_acc(data['username'], data['email'], data['password'])
    return jsonify(response), 201
    
