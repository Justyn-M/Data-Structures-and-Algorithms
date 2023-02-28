#
# stack_n_queue_lists.py - classes for a stack and queue using a linked list
#

from linkedLists import *


class DSAStack():

    def __init__(self):
        self.stack = DSALinkedList()

    def isEmpty(self) -> bool:
        return self.stack.isEmpty()

    def push(self, value: object):
        self.stack.insertFirst(value)

    def pop(self) -> object:
        return self.stack.removeFirst()

    def top(self) -> object:
        return self.stack.peekFirst()

    def __iter__(self):
        return self.stack.__iter__()

    def __reversed__(self):
        return self.stack.__reversed__()

    # print the stack
    def printStack(self):
        return str(self.stack)


class ShuffleQueue():

    def __init__(self):
        self.queue = DSALinkedList()

    def isEmpty(self) -> object:
        return self.queue.isEmpty()

    def enqueue(self, value: object):
        self.queue.insertLast(value)

    def dequeue(self) -> object:
        return self.queue.removeFirst()

    def peek(self) -> object:
        return self.queue.peekFirst()

    def __iter__(self):
        return self.queue.__iter__()

    def __reversed__(self):
        return self.queue.__reversed__()

    # print the queue
    def printQueue(self):
        return str(self.queue)


def main():
    print('Stack Test')
    print('==========')
    stack = DSAStack()
    stack.push('DSA')
    stack.push('Is')
    stack.push('Fun')
    stack.pop()
    stack.top()
    stack.isEmpty()
    stack.__iter__()
    stack.__reversed__()
    print(stack.printStack())

    print('Queeue Test')
    print('==========')
    queue = ShuffleQueue()
    queue.enqueue('DSA')
    queue.enqueue('is')
    queue.enqueue('fun')
    queue.dequeue()
    queue.peek()
    queue.isEmpty()
    queue.__iter__()
    queue.__reversed__()
    print(queue.printQueue())


if __name__ == "__main__":
    main()
