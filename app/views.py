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
    login_data = request.get_json()
    response = login_details.login(login_data)
    return jsonify(response), 201

@app.route('/v1/logout/', methods=['POST'])
def logout():
    """ Logs out a user """
    return jsonify("You are logged out")

@app.route('/v1/businesses/', methods=['POST'])
def register_business():
    """Register a business """
    business_details = WeConnect()
    business_data = request.get_json()
    response = business_details.register_business(business_data)
    return jsonify(response), 201

@app.route('/v1/reset-password/', methods=['POST'])
def password_reset():
    """ Password reset """
    passwd_reset_details = WeConnect()
    password_data = request.get_json()
    response = passwd_reset_details.reset_password(password_data)
    return jsonify(response), 201

@app.route('/v1/businesses/<businessid>', methods=['PUT'])
def update_a_business(businessid):
    """ Updates a business profile """
    update_a_business_details = WeConnect()
    businessid = request.get_json()
    response = update_a_business_details.update_business(businessid)
    return jsonify(response), 200

@app.route('/v1/businesses/<businessid>', methods=['DELETE'])
def delete_a_business(businessid):
    """ Removes a business """
    business_details = WeConnect()
    businessid = request.get_json()
    response = business_details.delete_business(businessid)
    return jsonify(response), 200

#TODO:
@app.route('/v1/businesses/', methods=['GET'])
def display_all_businesses():
    """ Retrieves all business prfiles"""
    pass

@app.route('/v1/businesses/<businessid>', methods=['GET'])
def display_a_business():
    """ Retrieves a business profile """
    pass

@app.route('/v1/businesses/<businessid>/reviews', methods=['POST'])
def add_a_review():
    """ Add a review for a business """
    pass

@app.route('/v1/businesses/<businessid>/reviews', methods=['GET'])
def list_all_business_reviews():
    """ Get all reviews for a business """
    pass 
    
