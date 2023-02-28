#
# Q4PQueueTest.py - Test Harness using built-in python priority queue
# source: https://docs.python.org/3/library/queue.html

from queue import PriorityQueue

if __name__ == '__main__':
    pq = PriorityQueue()

    pq.put((2, 'love'))
    pq.put((1, 'I'))
    pq.put((4, 'DSA'))
    pq.put((5, 'unit'))

    if pq.put((3, 'the')) == False:
        raise Exception('put failed')
    else:
        print('Put succeeded')

    print("\nThe number of objects in the queue is:", pq.qsize())
    print("\nTrue or False, The queue is empty:", pq.empty())

    while pq.empty() == False:
        print(pq.get())

    print("\nTrue or False, The queue is empty:", pq.empty())
