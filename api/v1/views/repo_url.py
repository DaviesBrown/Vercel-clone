#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/deploy', methods=['GET'], strict_slashes=False)
def deploy():
    """ Status of API """
    repo_url = request.args.get('repo_url')
    return jsonify({"status": "repo_url"})
