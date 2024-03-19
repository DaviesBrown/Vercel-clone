from uuid import uuid4

def generate() -> str:
    """ generates random id for the session """
    return str(uuid4())
