from collections import deque
class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, item):
        if not self.queue1:
            self.queue1.append(item)
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
        else:
            self.queue2.append(item)
            while self.queue1:
                self.queue2.append(self.queue1.popleft())

    def pop(self):
        if not self.queue1 and not self.queue2:
            return None
        return self.queue1.popleft() if self.queue1 else self.queue2.popleft()

    def print_stack(self):
        for item in self.queue1:
            print(item, end=" ")
        for item in reversed(self.queue2):
            print(item, end=" ")
        print()

stack = StackUsingQueues()
stack.push(8)
stack.push(3)
stack.push(4)
stack.push(7)
stack.push(6)
stack.push(1)
stack.print_stack()
stack.pop()
stack.print_stack()

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def printqueue(self):
        temp_stack = self.stack1.copy()
        temp_stack.reverse()
        print("Queue:", self.stack2 + temp_stack)


queue = QueueUsingStacks()
queue.enqueue(8)
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(1)
queue.printqueue()
print(f"Dequeue: {queue.dequeue()}")
queue.printqueue()


def balancedParentheses(str):
    stack = []
    open_set = {'(', '[', '{'}
    close_set = {')': '(', ']': '[', '}': '{'}

    for s in str:
        if s in open_set:
            stack.append(s)
        elif s in close_set:
            if not stack or stack.pop() != close_set[s]:
                return False

    return not stack


balanced_string = "{[()])}"
if balancedParentheses(balanced_string):
    print(f"'{balanced_string}' is balanced.")
else:
    print(f"'{balanced_string}' is not balanced.")