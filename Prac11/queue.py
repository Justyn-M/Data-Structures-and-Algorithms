from abc import abstractmethod
from collections import deque


class DSAQueue():
    @abstractmethod
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()
    
    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def __iter__(self):
        return self.queue.__iter__()


if __name__ == "__main__":
    q = DSAQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)

    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.isEmpty())
    