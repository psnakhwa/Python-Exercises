class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []
        
    def enqueue(self,a):
        self.inbox.append(a)
        
    def dequeue(self):
        if self.inbox == []:
            if self.outbox == []:
                return -1
        
        if self.outbox == []:
            while self.inbox != []:
                self.outbox.append(self.inbox.pop())
        self.outbox.pop()
      
    def printqueue(self):
        print self.outbox[0]
        
t = input()
Q = Queue()
for __ in range(t):
    arr = map(int,raw_input().split())
    if arr[0]==1:
        Q.enqueue(arr[1])
    elif arr[0]==2:
        Q.dequeue()
    elif arr[0]==3:
        Q.printqueue()