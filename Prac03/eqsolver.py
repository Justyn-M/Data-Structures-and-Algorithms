from stack_queue import *

def _ITPparse(eq: str) -> DSAQueue:
    token = eq.split(' ')
    stack = DSAStack(len(token))
    queue = ShuffleQueue(len(token))

    for i in range(len(token)):
        if token[i].isdigit():
            queue.enqueue(token[i])
        elif token[i] == '(':
            stack.push(token[i])
        elif token[i] == ')':
            while stack.top() != '(':
                queue.enqueue(stack.pop())
            stack.pop()
        elif token[i] == '+' or token[i] == '-':
            while not stack.isEmpty() and stack.top() != '(':
                queue.enqueue(stack.pop())
            stack.push(token[i])
        elif token[i] == '*' or token[i] == '/':
            while not stack.isEmpty() and (stack.top() == '*' or stack.top() == '/'):
                queue.enqueue(stack.pop())
            stack.push(token[i])
        elif token[i] == '^':
            while not stack.isEmpty() and stack.top() == '^':
                queue.enqueue(stack.pop())
            stack.push(token[i])
        else:
            raise Exception("Invalid token")

    while not stack.isEmpty():
        queue.enqueue(stack.pop())
    return queue

# solve postfix

def _PostfixSolver(queue: DSAQueue) -> float:
    stack = DSAStack(queue.getCount())
    while not queue.isEmpty():
        token = queue.dequeue()
        if token.isdigit():
            stack.push(float(token))
        elif token == '+':
            stack.push(stack.pop() + stack.pop())
        elif token == '-':
            stack.push(-stack.pop() + stack.pop())
        elif token == '*':
            stack.push(stack.pop() * stack.pop())
        elif token == '/':
            stack.push(1/stack.pop() * stack.pop())
        elif token == '^':
            stack.push(stack.pop() ** stack.pop())
        else:
            raise Exception("Invalid token")

    return stack.pop()

def solve(eq: str) -> float:
    return _PostfixSolver(_ITPparse(eq))

# test
if __name__ == "__main__":
    print(solve("2 + 3 * 4"))
    print(solve("2 + 3 * 4 / 2"))
    print(solve("2 + 3 * 4 / 2 ^ 2"))
    print(solve("2 + 3 * 4 / 2 ^ 2 - 1"))
    