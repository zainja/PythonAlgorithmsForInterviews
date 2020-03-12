class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # add to the end of the string
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.get_stack())
