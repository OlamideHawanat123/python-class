from inspect import stack


class Stack:
    stack = []
    size = 0
def is_empty():
    return stack == []

def push(element):
    stack.append(element)

