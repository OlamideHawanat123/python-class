stack = []
def is_empty():
    return stack == []


def push(element):
    stack.append(element)


def pop():
    stack.pop()


def peek():
    # if is_empty():
    #     raise IndexError("No element found")
    # else:
    return stack[-1]

def length():
    return len(stack)