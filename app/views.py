#!/usr/bin/env python3
""" Routes for app Tells lask what to display on which path """

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
    user_details = WeConnect()

    user_data = request.get_json()
    response = user_details.create_user(user_data)
    return jsonify(response), 201
    
@app.route('/v1/login/', methods=['POST'])
def login():
    """ Logs in a user """
    login_details = WeConnect()
    
    login_data= request.get_json()
    response = login_details.login(login_data)
    return jsonify(response), 201

@app.route('/v1/logout/', methods=['POST'])
def logout():
    """ Logs out a user """
    return jsonify("You are logged out")

@app.route('/v1/businesses/', methods=['POST'])
def register_biz():
    """Register a business """
    business_details = WeConnect()
    
    business_data = request.get_json()
    response = business_details.register_business(business_data)
    return jsonify(response), 201