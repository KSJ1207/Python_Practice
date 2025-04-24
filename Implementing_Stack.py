class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
        ## return self.items == []


my_stack = Stack()
my_stack.push(3)
my_stack.push(7)
my_stack.push(8)
my_stack.pop()

print(my_stack.items)

my_stack.push(5)
my_stack.push(6)

print(my_stack.size()) ## size(length) 확인
print(my_stack.items) ## 최종 stack