class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next
        print

def mergelists(a , b):
    n = Node(None)
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        n = a
        n.next = mergelists(a.next,b)
    if a.data >= b.data:
        n = b
        n.next = mergelists(a,b.next)
    return n

l1 = LinkedList()
l2 = LinkedList()
l1.push(25)
l1.push(15)
l1.push(5)
l2.push(30)
l2.push(20)
l2.push(10)
l1.printlist()
l2.printlist()
nhead = mergelists(l1.head,l2.head)
print
while nhead:
    print nhead.data,
    nhead = nhead.next


