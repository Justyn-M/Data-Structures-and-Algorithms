import numpy as np
from abc import abstractmethod


class DSAStack():
    DEFAULT_CAPACITY = 100
# main constructor

    def __init__(self):
        self.stack = np.empty(DSAStack.DEFAULT_CAPACITY, dtype=object)
        self.count = 0
# alternative constructor

    def __init__(self, capacity: int):
        self.stack = np.empty(capacity, dtype=object)
        self.count = 0

    def getCount(self) -> int:
        return self.count

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.stack)

    def push(self, value: object):
        if self.isFull():
            raise Exception("Stack is full")
        self.stack[self.count] = value
        self.count += 1

    def pop(self) -> object:
        topVal = self.top()
        self.count -= 1
        return topVal

    def top(self) -> object:
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.count-1]

    def printStack(self) -> None:
        print("Stack: ", end="")
        for i in range(self.count):
            print(self.stack[i], end=" ")

# parent class


class DSAQueue():
    @abstractmethod
    def getCount() -> int:
        pass

    @abstractmethod
    def isEmpty() -> bool:
        pass

    @abstractmethod
    def isFull() -> bool:
        pass

    @abstractmethod
    def enqueue(value: object):
        pass

    @abstractmethod
    def enqueue(value: object):
        pass

    @abstractmethod
    def printQueue():
        pass

# subclass 1


class ShuffleQueue(DSAQueue):
    DEFAULT_CAPACITY = 100
# main constructor

    def __init__(self):
        self.queue = np.empty(DSAQueue.DEFAULT_CAPACITY, dtype=object)
        self.count = 0
# alternative constructor

    def __init__(self, capacity: int):
        self.queue = np.empty(capacity, dtype=object)
        self.count = 0

    def getCount(self) -> object:
        return self.count

    def isEmpty(self) -> object:
        return self.count == 0

    def isFull(self) -> object:
        return self.count == len(self.queue)

    def enqueue(self, value: object):
        self.queue[self.count] = value
        self.count += 1

    def dequeue(self) -> object:
        value = self.queue[0]
        self.count -= 1
        for i in range(self.count):
            self.queue[i] = self.queue[i+1]
        return value

    def peek(self) -> object:
        return self.queue[0]

    def printQueue(self):
        print("Queue: ", end="")
        for i in range(self.count):
            print(self.queue[i], end=" ")

# subclass 2


class DSACircQueue(DSAQueue):
    DEFAULT_CAPACITY = 100

    def __init__(self):
        self.queue = np.empyty(DSACircQueue.DEFAULT_CAPACITY)
        self.head = 0
        self.count = 0

    def __init__(self, capacity: int):
        self.queue = np.empty(capacity, dtype=object)
        self.head = 0
        self.count = 0

    def getCount(self) -> int:
        return self.count

    def isEmpty(self) -> object:
        return self.count == 0

    def isFull(self) -> object:
        return self.count == len(self.queue)

    def enqueue(self, value: object):
        self.queue[(self.head + self.count) % len(self.queue)] = value
        self.count += 1

    def dequeue(self) -> object:
        self.count -= 1
        self.head = (self.head + 1) % len(self.queue)
        return self.queue[self.head - 1]

    def peek(self) -> object:
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue[self.head]

    def printQueue(self):
        print("Queue: ", end="")
        for i in range(self.count):
            print(self.queue[i], end=" ")


def _fibRecursive(DSAstack, n):
    n = 0

    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = _fibRecursive(n-1) + _fibRecursive(n-2)
    return DSAstack.push(fibVal)


def main():
    print("Stack Test")
    stack = DSAStack(capacity=5)
    stack.getCount()
    stack.isEmpty()
    stack.isFull()
    stack.push('DSA')
    stack.push(2)
    stack.push(3.14)
    stack.push(True)
    stack.push(5)
    print(stack.pop())
    print(stack.top())
    stack.printStack()
    print()

    print("Queue Test")
    queue = ShuffleQueue(capacity=5)
    queue.enqueue('DSA')
    queue.enqueue(2)
    queue.enqueue(3.14)
    queue.enqueue(True)
    queue.enqueue(5)
    queue.dequeue()
    queue.peek()
    queue.getCount()
    queue.isEmpty()
    queue.isFull()

    queue.printQueue()
    print()

    print("Circular Queue Test")
    circQueue = DSACircQueue(capacity=5)
    circQueue.enqueue('DSA')
    circQueue.enqueue(2)
    circQueue.enqueue(3.14)
    circQueue.enqueue(True)
    circQueue.enqueue(5)
    print(queue.dequeue())
    print(queue.peek())
    print(queue.getCount())
    print(queue.isEmpty())
    print(queue.isFull())
    circQueue.printQueue()
    print()

    print("Fibonacci Test")
    fibStack = DSAStack(capacity=5)
    _fibRecursive(fibStack, 5)
    fibStack.printStack()


if __name__ == "__main__":
    main()
