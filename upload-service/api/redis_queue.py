#!/usr/bin/python3
import redis


class Queue:
    def __init__(self) -> None:
        self.publisher = redis.Redis()

    def push(self, name: str, id: str):
        self.publisher.lpush(name, id)

    def get(self, id: str):
        return self.publisher.hget("status", id)

    def set(self, id: str, item: str):
        self.publisher.hset("status", id, item)
