#!/usr/bin/python3
import boto3
from boto3.s3 import transfer
from botocore.exceptions import ClientError
import logging
import os
from typing import List
from uuid import uuid4


def generate() -> str:
    """ generates random id for the session """
    return str(uuid4())


def get_transfer_client() -> transfer.S3Transfer:
    """ returns a transfer client """
    s3_client = boto3.client("s3")
    transfer_client = transfer.S3Transfer(s3_client)
    return transfer_client

def get_all_files(path: str) -> List[str]:
    """ gets all the paths of files stored in out/id dir """
    paths: list[str] = []
    for dir, subdirs, files in os.walk(path):
        for file in files:
            file_path = f"{dir}/{file}"
            paths.append(file_path)
    return paths

def upload_file_to_S3(filepath: str, bucket: str) -> bool:
    """ Uploads file to S3 given a path """
    object_name = os.path.basename(filepath)
    transfer_client = get_transfer_client()
    try:
        pass
        transfer_client.upload_file(filepath, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
