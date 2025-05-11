class Stack:
    my_stack = []

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self, element):
        return self.stack.pop(element)

    def peek(self):
        return self.stack[-1]
    