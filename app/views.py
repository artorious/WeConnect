#!/usr/bin/env python3
""" Routes for app. Tells lask what to display on which path """

from flask import request, jsonify
from app.models import WeConnect
from app import app

@app.route('/v1/', methods=['GET'])
def index(): 
    """ Return method made by the user to request resource """
    return str(request.method)
    
