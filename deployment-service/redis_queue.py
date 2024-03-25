#!/usr/bin/python3
import redis

class Queue:
    def __init__(self) -> None:
        self.subscriber = redis.Redis()
    
    def push(self, name: str, id: str):
        self.subscriber.lpush(name, id)
    
    def pop(self, name: str) -> str:
        return self.subscriber.rpop(name)
