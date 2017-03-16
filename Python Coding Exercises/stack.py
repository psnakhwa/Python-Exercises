from sys import maxsize

#Implementation of stack using arrays
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print "Cannot pop"
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.items[len(self.items) - 1]

#Implementation of Stack using Linked List
class Stacknode():
    def __init__(self,data):
        self.data = data
        self.next = None
class LLStack():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self,data):
        newnode = Stacknode(data)
        newnode.next = self.head
        self.head = newnode
        print "%d pushed into stack" %(data)

    def pop(self):
        if self.isEmpty():
            return
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.head.data

# Driver to check the implementations        
s = Stack()
s.isEmpty()
s.push(10)
s.push(20)
s.push(30)
print s.pop()
print "top of stack:",s.peek()
print s.pop()
print "top of stack:",s.peek()
print s.pop()
print "top of stack",s.peek()
print
s = LLStack()
s.isEmpty()
s.push(10)
s.push(20)
s.push(30)
print s.pop()
print "top of stack:",s.peek()
print s.pop()
print "top of stack:",s.peek()
print s.pop()
print "top of stack",s.peek()
