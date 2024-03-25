from redis_queue import Queue

worker = Queue()

def pop():
    id = worker.pop("build-queue")
    return id

def main() -> None:
    """ pulls value from redis queue"""
    id = pop()
    while id is not None:
        print(id)
        id = pop()
    
if __name__ == "__main__":
    main()