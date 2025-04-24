class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        ## self.items.insert(0, item) // 어디에 넣을지, 뭐를 넣을지지

    def dequeue(self):
        return self.items.pop(0)
        ## return self.items.pop()

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
        ## return self.items == []


my_queue = Queue()
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.dequeue()

print(my_queue.items)

my_queue.enqueue(3)
my_queue.enqueue(6)

print(my_queue.peek())
print(my_queue.size())
print(my_queue.is_empty())

print(my_queue.items)

