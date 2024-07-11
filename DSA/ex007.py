from collections import deque
from time import sleep

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

orders = ['pizza','samosa','pasta','biryani','burger']
queue = Queue()
for ord in orders:
    print(f"Order Recieved {ord}")
    queue.enqueue(ord)
    sleep(1)

print(f"Prepairing Order \n")
while queue.is_empty() == False:
    print(queue.dequeue(), " Is ready")
    sleep(1)
