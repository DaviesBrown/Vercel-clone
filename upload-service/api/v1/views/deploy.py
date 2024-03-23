#!/usr/bin/python3
""" Deploy """
from api.v1.views import app_views
from api.utils import generate, get_all_files, upload_file_to_S3
from api import redis_pub
from flask import jsonify, request
import git
import os


@app_views.route('/deploy', methods=['GET'], strict_slashes=False)
def deploy():
    """ Deploying production code """
    repo_url = request.args.get('repo_url')
    session_id = generate()
    path = os.getcwd()
    path = os.path.split(path)[0]
    #git.Repo.clone_from(repo_url, f"{path}/out/{session_id}")
    #file_paths = get_all_files(f"out/{session_id}")
    new_repo = git.Repo(repo_url) #local deployment
    new_repo.clone(f"{path}/out/{session_id}")
    #map(upload_file_to_S3, file_paths)
    redis_pub.push("build-queue", session_id)
    redis_pub.set(session_id, "uploaded")
    return jsonify({"status": "files uploaded", "id": session_id})
