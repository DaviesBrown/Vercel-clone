#!/usr/bin/python3
import os
from typing import List
from uuid import uuid4

def generate() -> str:
    """ generates random id for the session """
    return str(uuid4())

def get_all_files(path: str) -> List[str]:
    """ gets all the paths of files stored in out/id dir """
    paths: list[str] = []
    for dir, subdirs, files in os.walk(path):
        for file in files:
            file_path = f"{dir}/{file}"
            paths.append(file_path)
    return paths
