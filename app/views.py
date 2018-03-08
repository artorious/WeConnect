#!/usr/bin/env python3
""" Routes for app - tells flask whst to display on which path """

from flask import request, jsonify
from app.models import Users, BusinessProfiles, BusinessReviews
from app import app

# Init
user_inst = Users()
business_inst = BusinessProfiles()
profile_inst = BusinessProfiles()

@app.route('/v1/auth/register', methods=['POST'])
def register_account():
    """ Creates a user account """
    pass

@app.route('/v1/auth/login', methods=['POST'])
def login():
    """ Logs in a user """
    pass

@app.route('/v1/auth/logout', methods=['POST'])
def logout():
    """ Logs out a user """
    pass

@app.route('/v1/auth/reset-password', methods=['POST'])
def password_reset():
    """ Password reset """
    pass

@app.route('/v1/businesses', methods=['POST'])
def register_business():
    """Register a business """
    pass

@app.route('/v1/businesses/<businessId>', methods=['PUT'])
def update_business():
    """ Updates a business profile """
    pass

@app.route('/v1/businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    """ Removes a business """
    pass

@app.route('/v1/businesses', methods=['GET'])
def display_all_businesses():
    """ Retrieves all business prfiles"""
    pass

@app.route('/v1/businesses/<businessId>', methods=['GET'])
def display_a_business(businessId):
    """ Retrieves a business profile """
    pass 

@app.route('/v1/businesses/<businessId>/reviews', methods=['POST'])
def add_a_review(businessid):
    """ Add a review for a business """
    pass 

@app.route('/v1/businesses/<businessId>/reviews', methods=['GET'])
def list_all_business_reviews(businessId):
    """ Get all reviews for a business """
    pass
