#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from api import redis_sub
from flask import jsonify, request


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of deployment """
    id = request.args.get("id")
    response: str = redis_sub.get(id).decode("utf-8")
    return jsonify({"status": response})
