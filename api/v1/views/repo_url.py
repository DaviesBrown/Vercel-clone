#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from api.utils import generate
from flask import jsonify, request
import git


@app_views.route('/deploy', methods=['GET'], strict_slashes=False)
def deploy():
    """ Status of API """
    repo_url = request.args.get('repo_url')
    session_id = generate()
    git.Repo.clone_from(repo_url, f"/out/{session_id}")
    return jsonify({"status": "repo_url"})
