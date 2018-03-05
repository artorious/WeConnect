#!/usr/bin/env python3
""" Routes for app. Tells lask what to display on which path """

from flask import request
from app import app

@app.route('/', methods=['GET'])
def index(): 
    """ Return method made by the user to request resource """
    pass
    

