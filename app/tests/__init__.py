#!/usr/bin/env python3
""" Initialization file """
from flask import Flask

# Init

app = Flask(__name__, instance_relative_config=True)

# Load views
from app import views

# Load config file
app.config.from_object('config')
