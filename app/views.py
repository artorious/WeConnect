#!/usr/bin/env python3
""" Routes for app Tells lask what to display on which path """

from flask import request, jsonify

from app.models import WeConnect
from app import app

business_inst = WeConnect()

@app.route('/v1', methods=['GET'])
def index(): 
    """ Return method made by the user to request resource """
    return jsonify(request.method)
    
@app.route('/v1/auth/register', methods=['POST'])
def register_user():
    """ Creates a user account """
    user_data = request.get_json()
    response = business_inst.create_user(user_data)
    return jsonify(response), 201
    
@app.route('/v1/auth/login', methods=['POST'])
def login():
    """ Logs in a user """
    login_data = request.get_json()
    response = business_inst.login(login_data)
    return jsonify(response), 201

@app.route('/v1/auth/logout', methods=['POST'])
def logout():
    """ Logs out a user """
    return jsonify("You are logged out")

@app.route('/v1/auth/businesses', methods=['POST'])
def register_business():
    """Register a business """
    business_data = request.get_json()
    response = business_inst.register_business(business_data)
    return jsonify(response), 201

@app.route('/v1/auth/reset-password', methods=['POST'])
def password_reset():
    """ Password reset """
    password_data = request.get_json()
    response = business_inst.reset_password(password_data)
    return jsonify(response), 201

@app.route('/v1/businesses/<businessid>', methods=['PUT'])
def update_a_business(businessid):
    """ Updates a business profile """
    businessid = request.get_json()
    response = business_inst.update_business(businessid)
    return jsonify(response), 200

@app.route('/v1/businesses/<businessid>', methods=['DELETE'])
def delete_a_business(businessid):
    """ Removes a business """
    businessid = request.get_json()
    response = business_inst.delete_business(businessid)
    return jsonify(response), 200

@app.route('/v1/businesses', methods=['GET'])
def display_all_businesses():
    """ Retrieves all business prfiles"""
    businesses = business_inst.list_all_businesses()
    return jsonify(businesses), 200


@app.route('/v1/businesses/<businessid>', methods=['GET'])
def display_a_business(businessid):
    """ Retrieves a business profile """
    businessid = request.get_json()
    response = business_inst.list_a_single_business(str(businessid))
    return jsonify(response), 200

@app.route('/v1/businesses/<businessid>/reviews', methods=['POST'])
def add_a_review(businessid):
    """ Add a review for a business """
    businessid = request.get_json()
    response = business_inst.add_a_review(str(businessid))
    return jsonify(response), 201

#TODO:
@app.route('/v1/businesses/<businessid>/reviews', methods=['GET'])
def list_all_business_reviews(businessid):
    """ Get all reviews for a business """
    pass
    
