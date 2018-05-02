class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def print(self):

        for item in reversed(self.items):
            print(item)
            print('-------')


my_stack = Stack()
print(my_stack.is_empty())
my_stack.push(6)
my_stack.push(5)
my_stack.push(7)
my_stack.push(2)
my_stack.push(9)
my_stack.print()
