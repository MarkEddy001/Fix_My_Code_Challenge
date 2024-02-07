#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint

# to fix the code, i changed url_prefix from /api/v1 to / because 
# this indicates the root of the routes
app_views = Blueprint("app_views", __name__, url_prefix="/")

from api.v1.views.index import *
