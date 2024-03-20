#!/usr/bin/python3
import redis

class Queue:
    def __init__(self) -> None:
        self.publisher = redis.Redis()
    
    def push(self, name: str, id: str):
        self.publisher.lpush(name, id)
